<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <script src="jquery.min.js"></script>
    <title>Welcome to VulnApp</title>
</head>

<body>
    <div class="container">
        <div class="content">
            <h1>Welcome To VulnApp</h1>
            <p>Login to view your dashboard.</p>
            <h2>Login</h3>
                <div class="column-50">
                    <p id="messagess">
                    </p>
                </div>
                <form id="login-form">
                    <div class="row">
                        <div class="column-15">
                            <label for="email">Email</label>
                        </div>
                        <div class="column-45">
                            <input id="email" type="email" name="mail" placeholder="Enter email">
                        </div>
                        <div class="column-40">
                            <a class="err"></a>
                        </div>
                    </div>
                    <div class="row">
                        <div class="column-15">
                            <label for="pwd">Password</label>
                        </div>
                        <div class="column-45">
                            <input id="pwd" type="password" name="pass" placeholder="Enter your password">
                        </div>
                    </div>
                    <div class="row">
                        <input id="sbutton" type="submit" value="Submit">
                    </div>
                </form>
        </div>
    </div>
</body>
<script type="text/javascript" src="script.js"></script>

</html>