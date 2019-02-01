import {
  HandlerInput,
  RequestInterceptor,
  ResponseInterceptor
} from "ask-sdk-core";
import { Response } from "ask-sdk-model";
import * as Settings from "./Settings";

export const LoggingRequestInterceptor: RequestInterceptor = {
  process(handlerInput: HandlerInput) {
    if (Settings.debug) {
      const jsonReq = handlerInput
        ? JSON.stringify(handlerInput.requestEnvelope, null, 2)
        : "** EMPTY **";
      console.log(`\n***** REQUEST *****\n${jsonReq}\n***** END REQUEST *****`);
    }
  }
};

export const LoggingResponseInterceptor: ResponseInterceptor = {
  process(handlerInput: HandlerInput, response?: Response) {
    if (Settings.debug) {
      const jsonResp = response
        ? JSON.stringify(response, null, 2)
        : "** EMPTY **";
      console.log(
        `\n***** RESPONSE *****\n${jsonResp}\n***** END RESPONSE *****`
      );
    }
  }
};
