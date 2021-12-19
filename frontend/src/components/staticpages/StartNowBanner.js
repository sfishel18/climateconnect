import { Container, Typography } from "@material-ui/core";
import React, {useContext, useEffect, useState} from "react";
import { getLocalePrefix } from "../../../public/lib/apiOperations";
import { makeStyles } from "@material-ui/core/styles";
import getTexts from "../../../public/texts/texts_optimized";
import UserContext from "../context/UserContext";
import LightBigButton from "./LightBigButton";

const useStyles = makeStyles((theme) => ({
  root: {
    paddingTop: theme.spacing(3),
    paddingBottom: theme.spacing(3),
    background: theme.palette.primary.main,
  },
  headline: {
    color: "white",
    maxWidth: 580,
    textAlign: "center",
    margin: "0 auto",
  },
  signUpButton: {
    margin: "0 auto",
  },
  buttonContainer: {
    display: "flex",
    justifyContent: "center",
    marginTop: theme.spacing(3),
  },
  yellow: {
    color: theme.palette.yellow.main,
  },
}));

export default function StartNowBanner({ h1ClassName, className }) {
  const classes = useStyles();
  const { locale } = useContext(UserContext);
  const [texts, setTexts] = useState({});

  useEffect(async () => {
    if (locale) {
      setTexts(await getTexts({ page: "landing_page", locale: locale, classes: classes}));
    }
  },[locale, classes]);

  return (
    <div className={`${classes.root} ${className}`}>
      <Container>
        <div>
          <Typography className={`${classes.headline} ${h1ClassName}`} component="h1">
            {texts.start_now_banner_text}
          </Typography>
        </div>
        <div className={classes.buttonContainer}>
          <LightBigButton
            href={getLocalePrefix(locale) + "/signup"}
            className={classes.signUpButton}
          >
            {texts.sign_up}
          </LightBigButton>
        </div>
      </Container>
    </div>
  );
}
