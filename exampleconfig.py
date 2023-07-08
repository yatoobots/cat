from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 625898978
    API_HASH = "8b0f2179ed27f83222d344bb6959d00c"
    # the name to display in your alive message
    ALIVE_NAME = "IZUMI"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://enhyjtvy:OaiDDiXlmFECv2NmmsReVq9yIdSU-5uX@lucky.db.elephantsql.com/enhyjtvy"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHwBu7c0SvKHQQYoFX-npJK1iXvCDJs1bxA28p5M37TIKnHxpBMBc1_NlVSxkWZkEWNrQ5yjOd2BjihD4m-W6by5is1_8wqLiC4dHjMrMIwLXR26_IhLsdYNI2RGiz7-2XBdFbJHnnp0aEnChaAsJAHCMmCIq1GbF0cTgMmfZSNbOTZlAihfp7gxGBt77WVbAIMJ13wysPr2GOJjpoOAVq708mz_CNGOVY_84g1dzK_XMzwk6bHOQaTGfodKfyEthRoBPk5qmwF8jvnHpEovwz3Y84C-lc241--FnHM_X8O5PUaibj-ii50AorNGXF4vhYHvPWf6HmZuZaPHJ1ZcWHnC9fc="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6347775370:AAEny5nKVo5gG8KzbgmIAG8aISG6QFlu3MA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -962837583
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
