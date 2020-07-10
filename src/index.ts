import { SkillBuilders } from "ask-sdk-core";
import * as Handlers from "./Handlers";
import * as Interceptors from "./Interceptors";

export const handler = SkillBuilders.custom()
  .addRequestHandlers(
      Handlers.LaunchRequestHandler,
      Handlers.DisplayMessageHandler,
      Handlers.CustomInterfaceEventHandler,
      Handlers.CustomInterfaceExpirationHandler,
      Handlers.HelpIntentHandler,
      Handlers.CancelAndStopIntentHandler,
      Handlers.SessionEndedRequestHandler
  )
  .addRequestInterceptors(Interceptors.LoggingRequestInterceptor)
  .addResponseInterceptors(Interceptors.LoggingResponseInterceptor)
  .addErrorHandlers(Handlers.ErrorOccurred)
  .lambda();