<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>MyFlix Video Library</title>
</head>
<body>
    <h1>MyFlix Video Library</h1>

    {% for genre, videos in videos_by_genre.items() %}
        <div class="video-container" id="{{ genre }}-container">
            <h2>{{ genre|capitalize }}</h2>

            {% for video in videos %}
                <div class="video">
                    <p>{{ video['title'] }}</p>
                    <a href="{{ url_for('watch_details', video_id=video['_id']) }}">Watch Details</a>
                    <video controls>
                        <source src="{{ video['url'] }}" type="video/mp4">
                        Your browser does not support the video .
                    </video>
                </div>
            {% endfor %}
        </div>
    {% endfor %}

</body>
</html>
