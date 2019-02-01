import { HandlerInput } from "ask-sdk-core";
import * as WebRequest from "web-request";

export async function sendCustomDriective(
  handlerInput: HandlerInput,
  customDirective: any
) {
  const token = handlerInput.requestEnvelope.context.System.apiAccessToken;
  const endPoint = handlerInput.requestEnvelope.context.System.apiEndpoint;
  const passthroughUrl = `${endPoint}/v1/directives/endpointmessages`;
  const requestId = handlerInput.requestEnvelope.request.requestId;
  const requestOptions = {
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    json: true
  };
  const body = {
    header: {
      requestId
    },
    directive: customDirective
  };

  console.log("=== URL ===");
  console.log(passthroughUrl);
  console.log("=== requestOptions ===");
  console.log(JSON.stringify(requestOptions, null, 2));
  console.log("=== body ===");
  console.log(JSON.stringify(body, null, 2));

  // This will return a 204 unless something has gone wonky
  const result = await WebRequest.post(passthroughUrl, requestOptions, body);

  const success: boolean = result.statusCode === 200 || result.statusCode === 204;

  if (!success) {
    console.log(
      `Gadget directive call failed with code: ${
        result.statusCode
      } and message: ${result.statusMessage}`
    );
  }

  return success;
}
