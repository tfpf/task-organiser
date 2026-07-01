from task_organiser.constants import AuthConstants
from task_organiser.schemas import SignupRequest, SignupResponse


class AuthService:
    def signup(self, _request: SignupRequest) -> SignupResponse:
        return SignupResponse(text=AuthConstants.signup_success)
