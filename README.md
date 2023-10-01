[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Bp585G7b)

<h2>1.Prerequisites.</h2> 
<p>Before you can use this application, you will need to ensure that you have Python installed on your system. If you don't have Python installed, you can visit the official Python website at python.org, and download for your OS.</p>


<h2>2.Set Up Environment (via Git command).</h2>
<p>Step 1. Create folder on your desktop. Name it as you wish. For example, "test".<br>
Step 2. Go to my github repository (https://github.com/ADA-GWU/understanding-the-systems-with-complex-connections-ShamsiyyaAlakbarova). <br>
Step 3. Press to green CODE button, and copy HTTPS link (https://github.com/ADA-GWU/understanding-the-systems-with-complex-connections-ShamsiyyaAlakbarova.git).<br>
Step 4. Open your terminal, and enter into your newly created folder "test". You can do this
by running these commands:<br>
cd Desktop<br>
cd test<br>
After running these two commands, you will be inside your "test" folder.<br>
Step 5. Next clone my repo by pasting copied HTTPS link. <br>
Run this command: git clone https://github.com/ADA-GWU/understanding-the-systems-with-complex-connections-ShamsiyyaAlakbarova.git<br>
Step 6. Run this command: cd understanding-the-systems-with-complex-connections-ShamsiyyaAlakbarova. Now you are in the repo, and can start to use the application.</p>

<p>P.S. if you encounter issues while trying to clone a repository using a Git command, you can indeed download the repository as a ZIP file from the repository's web page.</p>

<h2>3.Run the Application.</h2>
<p>Step 1. Open 4 terminal windows. 3 windows are for server, and 1 window is for client.<br>
Step 2. In each terminal window you should be inside the repo.<br> 
Commands: cd Desktop  => cd test => cd understanding-the-systems-with-complex-connections-ShamsiyyaAlakbarova<br>  
Step 3. In first terminal run this command: python server.py 9001<br>
Instead of 9001 you can specify any available port on ypur system.<br>
After running this command, you will see this output "Socket created for port 9001
Server is listening on port 9001". It means, that server is listening on your 9001 port.<br>
Step 4. Do this for other two terminal windows for server. For example, for second window python server.py 9002, for third window python server.py 9003<br>
Step 5. In fourth terminal, that is for client, run this command: python client.py 9001<br>
Here, you also specify your port number, that is listening. You will get this output "Socket created for port 9001
Connected to server on port 9001
Enter a number (or 'exit' to quit):"<br>
Step 6. Enter a number. You will see a doubled result of this number in first terminal window, where server is listening on port 9001.<br>
Step 7. Go to client again, and type exit. After you quit, you can specify another port number in the client.<br>
For example, 9002. You will run this command in the client window: python client.py 9002. <br>
After you will do the same steps, as step 5, and step 6.</p>

<p>As you can see, you specify your port both for server and client. Then client sends your input to those port, that you have indicated. If you indicated in client port 9003, you will see the result in according server window (with 9003 port listening).</p> 