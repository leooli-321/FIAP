window.watsonAssistantChatOptions = {
  integrationID: "70891e29-5a82-454f-a0ab-8b9ef288e7c0", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "e27db655-79b0-46f5-9df1-221e9de03b25", // The ID of your service instance.
  onLoad: async (instance) => {
    await instance.render();
  },
};
setTimeout(function () {
  const t = document.createElement("script");
  t.src =
    "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
    (window.watsonAssistantChatOptions.clientVersion || "latest") +
    "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});
