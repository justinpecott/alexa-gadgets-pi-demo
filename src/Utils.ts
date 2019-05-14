import { HandlerInput } from "ask-sdk-core";
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

  console.log("=== URL ===");
  console.log(passthroughUrl);
  console.log("=== requestOptions ===");
  console.log(JSON.stringify(requestOptions, null, 2));

  const result = await WebRequest.json<any>(passthroughUrl, requestOptions);

  console.log("=== ENDPOINTS RESULT ===");
  console.log(result);

  return result.endpoints || [];
}
