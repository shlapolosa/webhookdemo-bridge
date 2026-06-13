"""Realtime WEBHOOK BRIDGE (generated, RT-2). Consume declared CONSUME_* topics ->
handlers.to_event -> POST to the webhook engine (Svix) /app/<app>/msg, which fans
out HMAC-signed deliveries to externally-registered endpoints. NO produce.

Binding env (envFrom <webhook>-conn + <webhook>-svix-credentials):
  WEBHOOK_ENGINE_API, WEBHOOK_ADMIN_TOKEN, WEBHOOK_APP_ID,
  WEBHOOK_EVENTTYPE_<topic> (topic -> Svix event type).
Transport + default Svix sink via realtime-transport."""
import os
from realtime_transport import create_realtime_webhook_app
from src.handlers import to_event

SERVICE_NAME = os.getenv("WEBSERVICE_NAME", os.getenv("REALTIME_PLATFORM_NAME", "realtime-webhook"))

app = create_realtime_webhook_app(
    service_name=SERVICE_NAME,
    to_event=to_event,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
