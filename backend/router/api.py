import logging
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware


from endpoint.endpoint import router

logger = logging.getLogger(__name__)


app = FastAPI(title="backend")

origins= [
    'http://localhost:3000'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(router,prefix='/api',tags=["basicsetup"])