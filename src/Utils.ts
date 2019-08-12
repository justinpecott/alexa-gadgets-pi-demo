import { HandlerInput } from "ask-sdk-core";
import { v4 as uuid } from "uuid";
import * as WebRequest from "web-request";

export async function getConnectedEndpoints(
  handlerInput: HandlerInput
) {
  const token = handlerInput.requestEnvelope.context.System.apiAccessToken;
  const endPoint = handlerInput.requestEnvelope.context.System.apiEndpoint;
  const passthroughUrl = `${endPoint}/v1/endpoints`;
  const requestOptions = {
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    json: true
  };

  const result = await WebRequest.json<any>(passthroughUrl, requestOptions);

  console.log("=== ENDPOINTS RESULT ===");
  console.log(result);

  return result.endpoints || [];
}

export function buildStartInputHanlder(
    handlerInput: HandlerInput,
    timeout = 90000,
    terminate = false,
    namespace = "Custom.SenseHatGadget"
) {
    const attributesManager = handlerInput.attributesManager;
    const sessionAttributes = attributesManager.getSessionAttributes();
    sessionAttributes.token = uuid();
    attributesManager.setSessionAttributes(sessionAttributes);

    console.log("Storing new token: " + sessionAttributes.token);
    return {
        type: "CustomInterfaceController.StartEventHandler",
        token: sessionAttributes.token,
        expiration: {
            durationInMilliseconds: timeout,
            expirationPayload: {
                message: "This is a sample message. Game over! Would you like to hear your stats?"
            }
        } ,
        eventFilter: {
            filterExpression: {
                and: [
                    { "==": [{ var: "header.namespace"}, namespace]}
                ]
            },
            filterMatchAction: terminate ? "SEND_AND_TERMINATE" : "SEND"
        }
    };
}

export function buildStopInputHanlder(
    handlerInput: HandlerInput
) {
    const attributesManager = handlerInput.attributesManager;
    const sessionAttributes = attributesManager.getSessionAttributes();
    console.log("Retrieving existing token: " + sessionAttributes.token);
    return {
        type: "CustomInterfaceController.StopEventHandler",
        token: sessionAttributes.token
    };
}

export function buildDisplayCustomDirective(
    message: string,
    endpointId: string,
    namespace = "Custom.SenseHatGadget",
    name = "DisplayMessage",
) {
    return {
        type: "CustomInterfaceController.SendDirective",
        header: {
            namespace,
            name
        },
        endpoint: {
            endpointId
        },
        payload: {
            message
        }
    };
}
