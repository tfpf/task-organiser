from task_organiser import constants, schemas


class Auth:
    def signup(self, _request: schemas.SignupRequest) -> schemas.SignupResponse:
        return schemas.SignupResponse(text=constants.Auth.signup_success)
