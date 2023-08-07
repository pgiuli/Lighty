from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import dotenv
import os
import requests
import colors


dotenv.load_dotenv(dotenv.find_dotenv())

bot_username = os.getenv('TELEGRAM_USERNAME')
bot_token = os.getenv('TELEGRAM_TOKEN')

admin_id = os.getenv('ADMIN_ID')
api_token = os.getenv('API_TOKEN')


api_url = 'http://localhost:8300/lighty/set-values' 


#Use this if not using a docker install
#api_ip = os.getenv('API_IP')
#api_port = os.getenv('API_PORT')
#api_url = "http://{}:{}/lighty/set-values/".format(api_ip, api_port)


def update_api(hai = None, preset = None):
    params = {
    "token": api_token,
    "hai": hai,
    "preset": preset
}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        print("GET request successful!")
    else:
        print("GET request failed with status code: {}".format(response.status_code))


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Lighty bot initialized! Use /help to see the available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""-- Lighy Bot --\n/hai to send an alert\n/preset <preset> to change the current color preset\nSee more at: github.com/pgiuli/Lighty""")

async def send_hai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #print(update.message.chat.id, admin_id)
    if int(update.message.chat.id) == int(admin_id):
        print('Sending hai!!!')
        update_api(hai=True)
        await update.message.reply_text('Sending hai!!!')
    else:
        await update.message.reply_text('You do not have permission to run this command.')

async def set_preset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #print(update.message.chat.id, admin_id)
    if int(update.message.chat.id) == int(admin_id):
        selected_preset = "".join(context.args)
        if colors.emotions.get(selected_preset) is not None:
            print('Setting preset to {}'.format(selected_preset))
            update_api(preset=selected_preset)
            await update.message.reply_text('Setting preset to {}'.format(selected_preset))
        else:
            print('Invalid preset selected')
            await update.message.reply_text('Invalid preset {}. Please try again.'.format(selected_preset))
    else:
        await update.message.reply_text('You do not have permission to run this command.')

#Currently without use as common message handling is not enabled
def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()
    # if 'text' in processed:
        #that

    return "Please use '/' commands to interact with the device!"

#Currently without use as common message handling is not enabled
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'New message: User ({update.message.chat.id}) in {message_type}: "{text}"')

    response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



def start_bot():
    app = Application.builder().token(bot_token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('hai', send_hai))
    app.add_handler(CommandHandler('preset', set_preset))

    # Messages -- Enable line to use common messages
    #app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)
    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)


