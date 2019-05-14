import { ErrorHandler, HandlerInput, RequestHandler } from "ask-sdk-core";
import { Directive, IntentRequest, interfaces } from "ask-sdk-model";
import { v4 as uuid } from "uuid";
import * as Utils from "./Utils";

/**
 * Handles 'Alexa, open ...'. Just give some general info to point the user in the right direction.
 */
export const LaunchRequestHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        return handlerInput.requestEnvelope.request.type === "LaunchRequest";
    },
    async handle(handlerInput: HandlerInput) {
        const attributesManager = handlerInput.attributesManager;
        const sessionAttributes = attributesManager.getSessionAttributes();
        sessionAttributes.token = uuid();
        sessionAttributes.endpoints = await Utils.getConnectedEndpoints(handlerInput);
        attributesManager.setSessionAttributes(sessionAttributes);

        const speechText =
            "Welcome to Sense Hat! You can tell me to display a message. " +
            "Otherwise I'll just be listening for interesting things that might occur.";

        const startEventHandlerDirective = {
            type: "CustomInterfaceController.StartEventHandler",
            token: sessionAttributes.token,
            expiration: {
                durationInMilliseconds: 60000,
                expirationPayload: {
                    message: "This is boring. I'm out!"
                }
            },
            eventFilter: {
                filterExpression: {
                    and: [
                        { "==": [{ var: "header.namespace"}, "Custom.SenseHatGadget"]},
                        { "==": [{ var: "endpoint.endpointId" }, sessionAttributes.endpoints[0].endpointId]}
                    ]
                },
                filterMatchAction: "SEND_AND_TERMINATE"
            }
        };

        return handlerInput.responseBuilder
            .speak(speechText)
            .addDirective(startEventHandlerDirective as Directive)
            .withShouldEndSession(false)
            .getResponse();
    }
};

export const CustomInterfaceExpirationHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        const request = handlerInput.requestEnvelope.request;
        // @ts-ignore: Request Type not in SDK yet
        return request.type === "CustomInterfaceController.Expired";
    },
    handle(handlerInput: HandlerInput) {
        const request = handlerInput.requestEnvelope.request;
        // @ts-ignore: Request Type (w/ expirationPayload) not in SDK yet
        const speechText = (request.expirationPayload == null)
            // @ts-ignore: Request Type (w/ expirationPayload) not in SDK yet
            ? "expiration payload data is missing" : request.expirationPayload.message;
        return handlerInput.responseBuilder.speak(speechText).withShouldEndSession(true).getResponse();
    }
};

export const CustomInterfaceEventHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        const request = handlerInput.requestEnvelope.request;
        // @ts-ignore: Request Type not in SDK yet
        return request.type === "CustomInterfaceController.EventsReceived";
    },
    handle(handlerInput: HandlerInput) {
        let speechText = "";
        // @ts-ignore: Request Type not in SDK yet
        const customEvents = handlerInput.requestEnvelope.request.events;
        for (const customEvent of customEvents) {
            if (customEvent.header.namespace === "Custom.SenseHatGadget" &&
                customEvent.header.name === "VoiceResponse") {
                // @ts-ignore: Custom Event not in SDK yet
                const payload = JSON.parse(customEvent.payload);
                speechText = payload.message;
            } else {
                console.log("=== UNKNOWN EVENT ===\n" + customEvent);
                speechText = "That was weird. I don't know anything about that event. Better check the logs.";
            }
        }

        return handlerInput.responseBuilder
            .speak(speechText)
            .getResponse();
    }
};

export const DisplayMessageHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        const request = handlerInput.requestEnvelope.request;
        return (
            request.type === "IntentRequest" &&
            request.intent.name === "DisplayMessageIntent"
        );
    },
    async handle(handlerInput: HandlerInput) {
        const attributesManager = handlerInput.attributesManager;
        const sessionAttributes = attributesManager.getSessionAttributes();
        const request = handlerInput.requestEnvelope.request as IntentRequest;
        const speechText =
            request.intent.slots && request.intent.slots.message
                ? request.intent.slots.message.value
                : "?";
        const tone =
            "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_positive_response_01'/>";

        let response = null;
        if (sessionAttributes.endpoints.length === 0) {
            console.log("No connected endpoints available");
            response = handlerInput.responseBuilder
                .speak(
                    "No endpoints found. Please try again after connecting your gadget."
                )
                .getResponse();
        } else {
            const customDirective = {
                type: "CustomInterfaceController.SendDirective",
                header: {
                    namespace: "Custom.SenseHatGadget",
                    name: "DisplayMessage"
                },
                endpoint: {
                    endpointId: (sessionAttributes.endpoints[0] || {}).endpointId || ""
                },
                payload: {
                    message: speechText
                }
            };
            response = handlerInput.responseBuilder
                .speak(tone)
                .addDirective(customDirective as Directive)
                .getResponse();
        }
        return response;
    }
};

export const HelpIntentHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        return (
            handlerInput.requestEnvelope.request.type === "IntentRequest" &&
            (handlerInput.requestEnvelope.request.intent.name ===
                "AMAZON.HelpIntent" ||
                handlerInput.requestEnvelope.request.intent.name ===
                "AMAZON.FallbackIntent")
        );
    },
    handle(handlerInput: HandlerInput) {
        const speechText =
            "Tell to display message followed by the message to display!";

        return handlerInput.responseBuilder
            .speak(speechText)
            .reprompt(speechText)
            .getResponse();
    }
};

export const CancelAndStopIntentHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        return (
            handlerInput.requestEnvelope.request.type === "IntentRequest" &&
            (handlerInput.requestEnvelope.request.intent.name ===
                "AMAZON.CancelIntent" ||
                handlerInput.requestEnvelope.request.intent.name ===
                "AMAZON.StopIntent")
        );
    },
    handle(handlerInput: HandlerInput) {
        const speechText = "Goodbye!";

        return handlerInput.responseBuilder.speak(speechText).getResponse();
    }
};

export const SessionEndedRequestHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
        return handlerInput.requestEnvelope.request.type === "SessionEndedRequest";
    },
    handle(handlerInput: HandlerInput) {
        return handlerInput.responseBuilder.getResponse();
    }
};

export const ErrorOccurred: ErrorHandler = {
    canHandle(handlerInput: HandlerInput, error: Error) {
        return true;
    },
    handle(handlerInput: HandlerInput, error: Error) {
        console.log("*************** ERROR ***************");
        console.log(JSON.stringify(error, Object.getOwnPropertyNames(error), 2));

        return handlerInput.responseBuilder
            .speak("Sorry, I can't understand the command. Please say again.")
            .reprompt("Sorry, I can't understand the command. Please say again.")
            .getResponse();
    }
};
