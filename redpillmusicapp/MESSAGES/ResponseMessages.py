class ResponseMessage:

    DEFAULT_ERROR = "Something went wrong"
    DEFAULT_SUCESS = "Completed successfully"
    DEFAULT_NOT_FOUND = "Not found"

    #LOGIN
    CREDENTIALS_REQUIRED = 'Email and password are required'
    INVALID_CREDENTIALS = 'Invalid email or password'
    USER_NOT_FOUND = 'User not found'

    LOGIN_SUCCESS = "Login successful"
    LOGIN_ERROR = "Login error"

    #register
    USERNAME_ALREADY_EXISTS = "Username already exists"

    #user
    USER_CREATED_SUCCESS = "User created successfully"
    USER_CREATED_ERROR = "User not created"

    USER_FOUND_ERROR = "User not found"
    USER_FOUND_SUCCESS = "User found successfully"

    #Artist
    ARTIST_CREATED_ERROR = "Artist not created"
    ARTIST_CREATED_SUCCESS = "Artist created successfully"

    ARTIST_DATA_FOUND_SUCCESS = "Artist data found"
    ARTIST_DATA_FOUND_ERROR = "Artist data not found"

    ONLY_ARTIST_CAN_UPDATE = "Only artist can update"

    ARTISTS_FOUND_ERROR = "Artists not found"

    ARTIST_FOUND_ERROR = "Artist not found"
    ARTIST_FOUND_SUCCESS = "Artist found successfully"

    ARTIST_UPDATED_SUCCESS = "Artist updated successfully"
    ARTIST_UPDATED_ERROR = "Artist not updated"

    ARTIST_DELETED_SUCCESS = "Artist deleted successfully"
    ARTIST_DELETED_ERROR = "Artist not deleted"

    #featured artist
    FEATURED_ARTIST_ADDED_SUCCESS = "Featured artist added successfully"
    FEATURED_ARTIST_ADDED_ERROR = "Featured artist not added"

    FEATURED_ARTIST_FOUND_ERROR = "Featured artist not found"
    FEATURED_ARTIST_FOUND_SUCCESS = "Featured artist found successfully"

    FEATURED_ARTIST_BY_GENRA_FOUND_ERROR = "Featured artist by genra not found"

    ARTIST_CORON_PROCESS_ERROR = "Featured artist coron process error"

    #genra
    GENRA_FOUND_ERROR = 'Genra not found'
    GENRA_FOUND_SUCCESS = 'Genra not found'

    ALL_GENRA_DATA_FOUND_SUCCESS = "All genra data found"
    ALL_GENRA_DATA_FOUND_ERROR = 'All Genra data not found'
    

    #song
    SONG_CREATED_ERROR = "Song not created"
    SONG_CREATED_SUCCESS = "Song created successfully"

    ALL_SONGS_FOUND_SUCCESS = "All songs found successfully"
    ALL_SONGS_FOUND_ERROR = "All songs not found"

    SONG_DATA_FOUND_SUCCESS = "Song data found successfully"
    SONG_DATA_FOUND_ERROR = "Song data not found"

    SONG_FOUND_ERROR = "Song not found"
    SONG_FOUND_SUCCESS = "Song found successfully"

    SONG_BY_GENRA_FOUND_ERROR = "Song by genra not found"
    SONG_BY_GENRA_FOUND_SUCCESS = "Song by genra found successfully"

    SONG_BY_ARTIST_FOUND_ERROR = "Song by artist not found"
    SONG_BY_ARTIST_FOUND_SUCCESS = "Song by artist found successfully"

    SONG_UPDATED_SUCCESS = "Song updated successfully"
    SONG_UPDATED_ERROR = "Song not updated"

    SONG_DELETED_SUCCESS = "Song deleted successfully"
    SONG_DELETED_ERROR = "Song not deleted"

    FEATURED_SONG_ADDED_SUCCESS = "Featured song added successfully"
    FEATURED_SONG_ADDED_ERROR = "Featured song not added"

    SONG_EMBEDED_LINK_ERROR = "Song embeded link not found"

    #featured songs
    FEATURED_SONG_FOUND_ERROR = "Featured song not found"
    FEATURED_SONG_FOUND_SUCCESS = "Featured song found successfully"

    SONG_CORON_PROCESS_ERROR = "Featured song coron process error"

    #Cron process
    CORON_PROCESS_SUCESS = "Coron process success"


