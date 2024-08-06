import sqlite3

def add_member(id, name, age):
    conn = sqlite3.connect('gym.db')  # Replace 'gym.db' with your database name
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (?, ?, ?)", (id, name, age))
        conn.commit()
        print(f"Member {name} added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM Members WHERE id = ?", (member_id,))
        member = cursor.fetchone()
        if member:
            cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)", 
                           (member_id, date, duration_minutes, calories_burned))
            conn.commit()
            print(f"Workout session for member {member_id} added successfully.")
        else:
            print(f"Error: Member ID {member_id} does not exist.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def update_member_age(member_id, new_age):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM Members WHERE id = ?", (member_id,))
        member = cursor.fetchone()
        if member:
            cursor.execute("UPDATE Members SET age = ? WHERE id = ?", (new_age, member_id))
            conn.commit()
            print(f"Age of member {member_id} updated to {new_age}.")
        else:
            print(f"Error: Member ID {member_id} does not exist.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def delete_workout_session(session_id):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM WorkoutSessions WHERE id = ?", (session_id,))
        session = cursor.fetchone()
        if session:
            cursor.execute("DELETE FROM WorkoutSessions WHERE id = ?", (session_id,))
            conn.commit()
            print(f"Workout session {session_id} deleted successfully.")
        else:
            print(f"Error: Workout session ID {session_id} does not exist.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Add a new member
    add_member(1, 'John Doe', 30)
    
    # Add a workout session
    add_workout_session(1, '2023-08-06', 60, 500)
    
    # Update member age
    update_member_age(1, 31)
    
    # Delete a workout session
    delete_workout_session(1)
