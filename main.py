def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass
videos=[]
while True :
    print('\n YouTube Manager | Choose an option below :')
    print("1. List all videos")
    print("2. Add a YouTube video")
    print("3. Update a YouTube video")
    print("4. Delete a YouTube video")
    print("5. Exit the app")
    choice=input("Enter your choice :")
    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)
        case '5':
            break
        case _:
            print("Invalid Choice!")