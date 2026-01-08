import gradio as gr
from sidekick import Sidekick

async def setup():
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick

async def process_message(sidekick, message, success_criteria, history):
    if sidekick is None:
        return [{"role": "system", "content": "Sidekick is not ready yet. Please wait..."}], sidekick
    
    if not message or not message.strip():
        return history, sidekick
    
    try:
        results = await sidekick.run_superstep(message, success_criteria, history)
        return results, sidekick
    except Exception as e:
        error_message = f"Error processing message: {str(e)}"
        print(error_message)
        if history is None:
            history = []
        history.append({"role": "system", "content": error_message})
        return history, sidekick

async def reset():
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    return "", "", [], new_sidekick

async def free_resources(sidekick):
    print("Cleaning up")
    try:
        if sidekick:
            await sidekick.cleanup()
    except Exception as e:
        print(f"Exception during cleanup: {e}")

with gr.Blocks(title = "Sidekick") as ui:
    gr.Markdown("## Sidekick Personal Co-Worker")
    sidekick = gr.State(delete_callback = free_resources)

    with gr.Row():
        chatbot = gr.Chatbot(label = "Sidekick", height = 300)
    with gr.Group():
        with gr.Row():
            message = gr.Textbox(show_label = False, placeholder = "Your request to the Sidekick")
        with gr.Row():
            success_criteria = gr.Textbox(
                show_label = False, placeholder = "What are your success critiera?"
            )
    with gr.Row():
        reset_button = gr.Button("Reset", variant = "stop")
        go_button = gr.Button("Go!", variant = "primary")

    ui.load(setup, outputs = [sidekick])
    
    async def submit_message(sidekick, message, success_criteria, history):
        if history is None:
            history = []
        return await process_message(sidekick, message, success_criteria, history)
    
    message_submit_event = message.submit(
        submit_message, 
        [sidekick, message, success_criteria, chatbot], 
        [chatbot, sidekick]
    )
    
    success_criteria_submit_event = success_criteria.submit(
        submit_message,
        [sidekick, message, success_criteria, chatbot],
        [chatbot, sidekick]
    )
    
    go_button_click_event = go_button.click(
        submit_message,
        [sidekick, message, success_criteria, chatbot],
        [chatbot, sidekick]
    )
    
    reset_button.click(
        reset, 
        outputs = [message, success_criteria, chatbot, sidekick]
    )

ui.launch(inbrowser = True, theme = gr.themes.Default(primary_hue = "emerald"))