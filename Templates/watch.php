<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Watch Video - MyFlix</title>
</head>
<body>
    <h1>Hello this is test</h1>
    <h2>{{ video_details['title'] }}</h2>
    <p>{{ video_details['description'] }}</p>

    <video controls>
        <source src="{{ video_details['url'] }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>