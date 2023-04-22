<!DOCTYPE html>

<html lang="en" style="height: 100%">
    <head>
        <meta charset="utf-8">
        <title>Language_flask_app.py : /home/Inoussa7/mysite/Language_flask_app.py : Editor : Inoussa7 : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Language_flask_app.py : /home/Inoussa7/mysite/Language_flask_app.py : Editor : Inoussa7 : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" />

        <link rel="stylesheet" href="/static/CACHE/css/output.ff34947502d6.css" type="text/css" media="screen">
        <link rel="stylesheet" href="/static/CACHE/css/output.b9a4961a16f7.css" type="text/css"><link rel="stylesheet" href="/static/CACHE/css/output.135dadead6d9.css" type="text/css" media="screen">

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "ZGILqpxFYQ7zoMWqohBIrx1R6dVkmupV0VniDetPkWdJxXyBxPxlNbqNNg3clFfM";
        </script>
        <script src="/static/CACHE/js/output.9912b9c89b96.js"></script>
        

        <script src="/static/CACHE/js/output.ce8d62eca661.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/Inoussa7/files/home/Inoussa7/mysite/Language_flask_app.py",
          check_hash: "/user/Inoussa7/files/home/Inoussa7/mysite/Language_flask_app.py",
          update_editor_mode_preference: "/user/Inoussa7/account/update_editor_mode_preference",
          console_api: "/api/v0/user/Inoussa7/consoles/",
        });
        var filename = "/home/Inoussa7/mysite/Language_flask_app.py";
        var hash = "e8dec778c32c58235d148acd4329266a";
        var interpreter = "python3.10";

        
            Anywhere.Editor.InitializeAce(ace, Anywhere.urls, filename, hash, interpreter, "pythonanywhere.com");
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/Inoussa7/files/sharing/",
            csrfToken: "ZGILqpxFYQ7zoMWqohBIrx1R6dVkmupV0VniDetPkWdJxXyBxPxlNbqNNg3clFfM",
            path: "/home/Inoussa7/mysite/Language_flask_app.py"
          }
        );

      });
    </script>

        

    </head>

     <body style="height:100%;">
       <div style="min-height: 100%; position: relative;">
        
        
  




  <nav class="navbar navbar-default fullscreen-main-navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">
        <img id="id_logo" src="/static/anywhere/images/PA-logo-snake-only.svg" height="100%" />
      </a>
    </div>

    <div class="extra-nav-content">
      

  <div id="id_editor_toolbar">

    <div class="pull-left">
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/Inoussa7/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/Inoussa7/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Inoussa7/files/home/Inoussa7" target="_parent">Inoussa7</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/Inoussa7/files/home/Inoussa7/mysite" target="_parent">mysite</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">Language_flask_app.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
    </div>

    <div id="id_editor_messages" class="pull-left">
      

    </div>

    <div class="pull-right">
      <div id="id_editor_buttons_right" class="form-inline">
        <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
        <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
        
          <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
          <select id="id_keybinding_mode_select" class="form-control input-sm">
            <option value="normal">Normal</option>
            <option value="vim">Vim</option>
          </select>
        
        <button id="id_display_sharing_options" class="btn btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
          <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
          Share
        </button>
        
          <button id="id_save" class="btn btn-success" title="Save (Ctrl + S)">
            <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
            Save
          </button>
          <button id="id_save_as" class="btn btn-default" title="Save As">Save as...</button>
        
        
          <button class="btn btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
        

        
          
            <form class="reload_web_app" style="display: flex" method="POST" action="/user/Inoussa7/webapps/Language_Learning-Inoussa7.pythonanywhere.com/reload">
              <button class="btn btn-default" type="submit" title="Reload Language_Learning-Inoussa7.pythonanywhere.com">
                <i class="glyphicon glyphicon-refresh"></i>
              </button>
              <img style="display: none;" class="spinner" src="/static/anywhere/images/spinner-small.gif" />
              <div style="display: none; clear: both;" class="alert alert-danger error_message generic_error">
                There was a problem. If this keeps happening, please <a href="" class="feedback_link">send us feedback</a>.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message slow_startup_error">
                Your webapp took a long time to reload. It probably reloaded, but we were unable to check it.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message virtualenv_error">
                There is a problem with your virtualenv setup. Look at the <b>virtualenv</b> section on the web app tab for details.
              </div>
              <div style="display: none; clear: both;" class="alert alert-danger error_message cname_error">
                There is a problem with your DNS configuration. Take a look at the <b>DNS setup</b> section on the web app tab for details.
              </div>
            </form>
          
        
      </div>
    </div>

  </div>


    </div>

    <div class="dropdown fullscreen-hamburger fullscreen-mini-nav">
      <button type="button" class="navbar-toggle" data-toggle="dropdown"  role="button" aria-haspopup="true" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <ul class="dropdown-menu pull-right">
        
  <li class=""><a id="id_dashboard_link" href="/user/Inoussa7/">Dashboard</a></li>
  <li class=""><a id="id_consoles_link" href="/user/Inoussa7/consoles/">Consoles</a></li>
  <li class=""><a id="id_files_link" href="/user/Inoussa7/files/home/Inoussa7">Files</a></li>
  <li class=""><a id="id_web_app_link" href="/user/Inoussa7/webapps/">Web</a></li>
  <li class=""><a id="id_tasks_link" href="/user/Inoussa7/tasks_tab/">Tasks</a></li>
  <li class=""><a id="id_databases_link" href="/user/Inoussa7/databases/">Databases</a></li>


        
<li class=""><a href="" target="_parent" class="feedback_link">Send feedback</a></li>


<li class=""><a href="/forums/" target="_parent" class="forums_link">Forums</a></li>
<li class=""><a href="https://help.pythonanywhere.com/" target="_parent" class="help_link">Help</a></li>
<li class=""><a href="https://blog.pythonanywhere.com/" target="_parent" class="blog_link">Blog</a></li>

  
  <li class=""><a href="/user/Inoussa7/account/" target="_parent" class="account_link">Account</a></li>
  <li class="">
    <form action="/logout/" method="POST" target="_parent">
      <input type="hidden" name="csrfmiddlewaretoken" value="ZGILqpxFYQ7zoMWqohBIrx1R6dVkmupV0VniDetPkWdJxXyBxPxlNbqNNg3clFfM">
      <button type="submit" class="btn-link logout_link">Log out</button>
    </form>
  </li>


      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">import os
from flask import Flask, render_template, request, jsonify
import openai
import speech_recognition as sr
import pyttsx3
import soundfile as sf
import io
import simpleaudio as sa
from playsound import playsound
import threading


import warnings
warnings.filterwarnings(&quot;ignore&quot;, message=&quot;The NumPy module was reloaded&quot;)



app = Flask(__name__)
app.config[&#39;UPLOAD_FOLDER&#39;] = os.path.join(os.getcwd(), &#39;audio_files&#39;)
openai.api_key = &quot;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&quot;
LANGUAGES = {
    &#39;english&#39;: &#39;en&#39;,
    &#39;french&#39;: &#39;fr&#39;,
}

# Set up Text-to-Speech API credentials
openai.api_key = &quot;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&quot;
model_engine = &quot;text-davinci-003&quot;
voice_engine = &quot;text-to-speech/mark&quot;

# Initialize the recognizer
r = sr.Recognizer()
GREETING_KEYWORDS = {
    &#39;en&#39;: [&#39;Hello!&#39;, &#39;Hi there!&#39;, &#39;Hey!&#39;],
    &#39;fr&#39;: [&#39;Bonjour!&#39;, &#39;Salut!&#39;, &#39;Coucou!&#39;],
}
dialogueArray = []

def build_prompt(text, language):
    prompt = f&quot;{text}\n&quot;
    if language == &#39;english&#39;:
        prompt += &quot;Ino: &quot;
    else:
        prompt += f&quot;Ino ({language}): &quot;
    return prompt


@app.route(&#39;/&#39;)
def home():
    return render_template(&#39;home.html&#39;, title=&#39;Home&#39;)

@app.route(&#39;/text&#39;)
def text():
    return render_template(&#39;text.html&#39;, title=&#39;Text&#39;)

@app.route(&#39;/speech&#39;)
def speech():
    return render_template(&#39;speech.html&#39;, title=&#39;Speech&#39;)

def generate_chat_response(user_input, lang):
    # Generate a response using OpenAI API
    prompt = build_prompt(user_input, lang)
    response = generate_response(prompt, lang)
    print(f&quot;Response ({lang}): {response}&quot;)

    # Speak the response using pyttsx3 library
    sayResponse(response)

    return jsonify({&#39;response&#39;: response})

@app.route(&#39;/chat&#39;, methods=[&#39;POST&#39;])
def chat():
    lang = request.form[&#39;language&#39;]

    # Check if the input is from text or speech
    if &#39;input_text&#39; in request.form:
        # Get the user input from the text form
        user_input = request.form[&#39;input_text&#39;]

    else:
        # Get the audio data from the speech form
        audio_data = request.form[&#39;audio_data&#39;]

        # Use SpeechRecognition library to transcribe the audio data
        r = sr.Recognizer()
        with sr.AudioFile(audio_data) as source:
            audio = r.record(source)
        try:
            user_input = r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return jsonify({&#39;error&#39;: &#39;Unable to recognize speech&#39;})

    if lang == &#39;en&#39;:
        response = generate_chat_response(user_input, lang)
    elif lang == &#39;fr&#39;:
        response = generate_chat_response(user_input, lang)
    else:
        return jsonify({&#39;error&#39;: &#39;Invalid language&#39;})

    return response

&quot;&quot;&quot;@app.route(&#39;/process_audio&#39;, methods=[&#39;POST&#39;])
def process_audio():
    lang = request.form.get(&#39;language&#39;)
    audio_file = request.files[&#39;audio_file&#39;]

    # Save the file synchronously
    file_path = os.path.join(app.config[&#39;/home/Inoussa7/audio_files&#39;], audio_file.filename)
    audio_file.save(file_path)
    print(&#39;File saved to:&#39;, file_path)

    # Continue with speech recognition
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        user_input = r.recognize_google(audio, language=LANGUAGES[lang])
    except sr.UnknownValueError:
        return jsonify({&#39;error&#39;: &#39;Unable to recognize speech&#39;})

    # Generate and speak the response
    response = generate_and_speak_response(user_input, lang)

    if &#39;output_audio&#39; in request.form:
        # Convert the response to speech using pyttsx3 library
        engine.save_to_file(response, &#39;output.mp3&#39;)
        engine.runAndWait()
        return send_file(&#39;output.mp3&#39;)
    else:
        # Return the response as text
        return jsonify({&#39;response&#39;: response})&quot;&quot;&quot;

def generate_response(prompt, language):
    engine = &quot;text-davinci-003&quot; if language == &#39;fr&#39; else &quot;text-davinci-003&quot;
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_and_speak_response(user_input, lang):
    # Generate a text response based on the user&#39;s input
    response = generate_chat_response(user_input, lang)

    # Convert the text response to speech using pyttsx3 library
    engine = pyttsx3.init()
    engine.setProperty(&#39;voice&#39;, voices[lang])
    engine.say(response)
    engine.runAndWait()

    return response

def sayResponse(response):
    engine = pyttsx3.init()
    engine.setProperty(&#39;voice&#39;, voice_engine)
    engine.setProperty(&#39;rate&#39;, 0)
    engine.say(response)
    engine.runAndWait()



if __name__ == &#39;main&#39;:
    app.run(debug=True)

</div>
      

      <div id="id_ide_console">
        
          <iframe src="/user/Inoussa7/consoles/28308340/frame/" id="id_console" name="console" class="soft_keyboard_sensitive">
          </iframe>
        
      </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
      <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
      <div class="dialog_buttons">
        <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
        <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
      </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
      <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
      <div class="dialog_buttons">
        <button id="id_force_save" class="btn btn-danger">Force Save</button>
        <button id="id_cancel_save" class="btn btn-default">Cancel</button>
      </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
      <form class="form-inline">
        <div class="form-group">
          <label for="id_save_as_path">Please enter a path:</label>
          <input id="id_save_as_path" class="form-control" style="width: 100%;" />
        </div>
        <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
        <p>
          <span id="id_save_as_error" class="error_message"></span>
        </p>
        <div class="dialog_buttons">
          <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
          <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
        </div>
      </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>


        
      </div>

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" style="display: none">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_rate_limit_error" style="display: none">
        Sorry, we have had to rate-limit your feedback sending.<br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_success" style="display: none">
        Thanks for the feedback! Our tireless devs will get back to you soon.
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
    <div id="id_feedback_dialog_only_close_button" style="display: none">
        <button class="btn btn-primary" id="id_feedback_dialog_close_button">Close</button>
    </div>
</div>


        
            <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-18014859-6', 'auto');
                ga('send', 'pageview');
            </script>
        

        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
