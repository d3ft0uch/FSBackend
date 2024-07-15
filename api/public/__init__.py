from fastapi import APIRouter, Depends

from api.auth import current_superuser
from api.public.user import views as users
from api.public.user_info import views as user_infos
from api.public.listing import views as listings
from api.public.listing_picture import views as listing_pictures
from api.public.user_messages_tg import views as user_messages_tg
from api.public.user_utm_sources import views as user_utm_sources
from api.public.user_access_requests import views as user_accept_requests
from api.public.payments import views as payments
from api.public.demands import views as demands
from api.public.trials import views as trials
from api.public.stripe_webhooks import views as stripe_webhooks


api = APIRouter()


api.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(authent)],
)

api.include_router(users.auth_router, prefix="/auth/jwt", tags = ["auth"],)

api.include_router(users.register_router, prefix="/auth", tags=["auth"], )

api.include_router(users.reset_password_router, prefix="/auth", tags=["auth"], )
api.include_router(users.verify_router, prefix="/auth", tags=["auth"], )
api.include_router(users.users_router, prefix="/users", tags=["users"], )
api.include_router(users.oauth_router, prefix="/auth/google", tags=["auth"], )
api.include_router(users.oauth_associate_router, prefix="/auth/associate/google", tags=["auth"], )



api.include_router(
    user_infos.router,
    prefix="/user_infos",
    tags=["UserInfos"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    listings.router,
    prefix="/listings",
    tags=["Listing"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    listing_pictures.router,
    prefix="/listing_pictures",
    tags=["ListingPictures"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    user_messages_tg.router,
    prefix="/user_messages_tg",
    tags=["UserMessagesTG"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    user_utm_sources.router,
    prefix="/user_utm_sources",
    tags=["UserUtmSources"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    user_accept_requests.router,
    prefix="/user_access_requests",
    tags=["UserAccessRequests"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    payments.router,
    prefix="/payments",
    tags=["Payments"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    demands.router,
    prefix="/demands",
    tags=["Demands"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    trials.router,
    prefix="/trials",
    tags=["Trials"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    stripe_webhooks.router,
    prefix="/stripe_webhooks",
    tags=["StripeWebhooks"],
    # dependencies=[Depends(authent)],
)