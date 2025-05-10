from contextlib import asynccontextmanager
from fastapi import FastAPI
from common.exception_handlers import add_exception_handlers
from calc_cdu.app.routes import cdu_endpoints
from calc_cdu.app.config import settings
from common.logging import configure_logging
from common.middleware import TraceMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---------- startup ----------
    configure_logging()                # logging config
    print(f"🌱  Starting {settings.project_name} "
          f"in {settings.environment}…")
    yield                              # ← la app queda sirviendo
    # ---------- shutdown ----------
    print("🌿  Shutting down calc‑cdu…")


app = FastAPI(title=settings.project_name, lifespan=lifespan)
configure_logging()
app.add_middleware(TraceMiddleware)
add_exception_handlers(app)
app.include_router(cdu_endpoints.router)


@app.get("/health")
async def health():
    """
    Health check endpoint para comprobar si el Cado de Uso está en 
    funcionamiento.
    """
    return {"message": "Fast API Skeleton is up!"}

