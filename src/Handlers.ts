import { ErrorHandler, HandlerInput, RequestHandler } from "ask-sdk-core";
import { Directive, IntentRequest } from "ask-sdk-model";
import * as Utils from "./Utils";

/**
 * Handles 'Alexa, open ...'. Just give some general info to point the user in the right direction.
 */
export const LaunchRequestHandler: RequestHandler = {
  canHandle(handlerInput: HandlerInput) {
    return handlerInput.requestEnvelope.request.type === "LaunchRequest";
  },
  handle(handlerInput: HandlerInput) {
    const speechText =
      "Welcome to Sense Hat! You can say display message followed by the message to display!.";

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(speechText)
      .getResponse();
  }
};

export const DisplayMessageHandler: RequestHandler = {
    canHandle(handlerInput: HandlerInput) {
      const request = handlerInput.requestEnvelope.request;
      return (
        request.type === "IntentRequest" && request.intent.name === "DisplayMessageIntent"
      );
    },
    async handle(handlerInput: HandlerInput) {
      const request = handlerInput.requestEnvelope.request as IntentRequest;
      const speechText = request.intent.slots && request.intent.slots.message ?
            request.intent.slots.message.value : "?";
      const tone = "<audio src='soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_positive_response_01'/>";

      const direcive = {
        type: "Alexa.Endpoints.SendMessage",
        namespace: "SenseHatGadget",
        name: "DisplayMessage",
        payload: {
          message: speechText
        }
      };

      const endpoints = await Utils.getConnectedEndpoints(handlerInput);

      let response = null;
      if (endpoints.length === 0) {
        console.log("No connected endpoints available");
        response = handlerInput.responseBuilder
            .speak("No endpoints found. Please try again after connecting your gadget.")
            .getResponse();
      } else {
        const customDirective = {
            type: "CustomInterfaceController.SendDirective",
            header: {
                name: "SenseHatGadget",
                namespace: "DisplayMessage"
            },
            endpoint: {
              endpointId: ((endpoints[0] || {}).endpointId || "")
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
    const speechText = "Tell to display message followed by the message to display!";

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

    return handlerInput.responseBuilder
      .speak(speechText)
      .getResponse();
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
