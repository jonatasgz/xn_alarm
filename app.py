import gradio as gr

def cll_alarm(alarm, score, lyx, lyy, lywy, lyz):
    if alarm < 180:
        if lyx < 79.6:
            message = "Normal/Reactive"
        else: 
            if score < 1.17:
                message = "No CLL. Slide review/Cytometry"
            else:
                if lyx/lywy < 0.093:
                    message = "No CLL. Slide review/Cytometry"
                else:
                    message = "CLL. Slide review/Cytometry"
    else:
        if score >= 1.17:
            message = "CLL. Slide review/Cytometry"
        else:
            if lyx <= 80.25:
                message = "Normal/Reactive"
            else:
                if lyy <= 70.15:
                    message = "Normal/Reactive"
                else:
                    if lyz <= 58.15:
                        message = "Normal/Reactive"
                    else:
                        message = "No CLL"
    return message

with gr.Blocks(title="XN Alarm for CLL") as calculator:
    with gr.Row():
        with gr.Column():
            alarm = gr.Number(label="XN Alarm")
            score = gr.Number(label="Score")
            lyx = gr.Number(label="Ly-x")
            lyy = gr.Number(label="Ly-y")
            lywy = gr.Number(label="Ly-wy")
            lyz = gr.Number(label="Ly-z")
            send_button = gr.Button("Submit")
        with gr.Column():
            output = gr.Textbox(label = 'Conclusion')
            send_button.click(fn=cll_alarm, inputs=[alarm, score, lyx, lyy, lywy, lyz], outputs=output, api_name='xn_alarm_cll')

calculator.launch()
