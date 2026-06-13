"""Realtime GATEWAY (generated, RT-2). Consumes the declared topics and streams
to websocket clients on /ws. Transport via realtime-transport; topics/bindings
from CONSUME_*/PRODUCE_* + <realtime>-conn env (realtime-service CD)."""
import os
from realtime_transport import create_realtime_agent_app, GenericRealtimeAgent

SERVICE_NAME = os.getenv("WEBSERVICE_NAME", os.getenv("REALTIME_PLATFORM_NAME", "realtime-service"))

app = create_realtime_agent_app(
    agent_class=GenericRealtimeAgent,
    service_name=SERVICE_NAME,
    description="Realtime websocket gateway (consume -> /ws)",
    endpoints=[],
    websocket_endpoints=[{"path": "/ws", "description": "realtime stream"}],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
