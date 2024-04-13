import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Switch, Redirect } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import Systems from "./components/systems/Systems";
import SystemDetailPage from "./components/systems/systemDetails"; // Import the SystemDetailPage component
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import LandingPage from "./components/LandingPage/LandingPage";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const sessionUser = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {isLoaded && (
        <>
          {sessionUser ? (
            <>
              <Navigation />
              <Switch>
                <Route exact path="/">
                  <Systems />
                </Route>
                <Route path="/systems/:id">
                  <SystemDetailPage />
                </Route>
                <Redirect to="/" />
              </Switch>
            </>
          ) : (
            <Switch>
              <Route exact path="/">
                <LandingPage />
              </Route>
              <Route path="/login">
                <LoginFormPage />
              </Route>
              <Route path="/signup">
                <SignupFormPage />
              </Route>
              <Redirect to="/" />
            </Switch>
          )}
        </>
      )}
    </>
  );
}

export default App;
