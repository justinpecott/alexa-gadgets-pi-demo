import { ErrorHandler, HandlerInput, RequestHandler } from "ask-sdk-core";
import { IntentRequest } from "ask-sdk-model";
import * as Utils from "./Utils";

const statusCodes: { [intentName: string]: number } = {
  LunchStatusIntent: 1,
  MeetingStatusIntent: 2,
  BusyStatusIntent: 3,
  TravelStatusIntent: 4,
  AvailableStatusIntent: 5
};

const statusMessages: { [intentName: string]: string } = {
  LunchStatusIntent: "Lunch",
  MeetingStatusIntent: "In a Meeting",
  BusyStatusIntent: "Busy",
  TravelStatusIntent: "Away of Travel",
  AvailableStatusIntent: "Available"
};

/**
 * Handles 'Alexa, open ...'. Just give some general info to point the user in the right direction.
 */
export const LaunchRequestHandler: RequestHandler = {
  canHandle(handlerInput: HandlerInput) {
    return handlerInput.requestEnvelope.request.type === "LaunchRequest";
  },
  handle(handlerInput: HandlerInput) {
    const speechText =
      "Welcome to Pi Time! You can say set status or send message.";

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(speechText)
      .getResponse();
  }
};

export const StatusIntentHandler: RequestHandler = {
  canHandle(handlerInput: HandlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return (
      request.type === "IntentRequest" && request.intent.name in statusCodes
    );
  },
  async handle(handlerInput: HandlerInput) {
    const request = handlerInput.requestEnvelope.request as IntentRequest;
    const statusCode = statusCodes[request.intent.name];
    let speechText = `Status set to ${statusMessages[request.intent.name]}`;

    const direcive = {
      type: "Alexa.Endpoints.SendMessage",
      namespace: "StatusGaugeGadget",
      name: "SetStatus",
      payload: {
        status: statusCode
      }
    };

    if (!Utils.sendCustomDriective(handlerInput, direcive)) {
      speechText = "Something went wrong, sorry!";
    }

    return handlerInput.responseBuilder
      .speak(speechText)
      .withSimpleCard("Pi Times Status Updated", speechText)
      .getResponse();
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
    const speechText = "You can say hello to me!";

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(speechText)
      .withSimpleCard("Hello World", speechText)
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
      .withSimpleCard("Hello World", speechText)
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
