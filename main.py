from pyscript import document

# this is an dictionary to hold all the valorant agents with thier info
agent_database = {
    # number keys
    "1": ("1", "Jett", "Sunwoo Han", "South Korea"),
    "2": ("2", "Reyna", "Zyanya Mondragón", "Mexico"),
    "3": ("3", "Omen", "Unknown", "Unknown"),
    "4": ("4", "Iso", "Li Zhao Yu", "China"),
    "5": ("5", "Fade", "Hazal Eyletmez", "Turkey"),
    "6": ("6", "Sova", "Sasha Novikov", "Russia"),
    "7": ("7", "Viper", "Sabine Callas", "United States"),
    "8": ("8", "Killjoy", "Klara Böhringer", "Germany"),
    "9": ("9", "Cypher", "Aamir El Amari", "Morocco"),
    "10": ("10", "Chamber", "Vincent Fabron", "France"),

    # name keys
    "JETT": ("1", "Jett", "Sunwoo Han", "South Korea"),
    "REYNA": ("2", "Reyna", "Zyanya Mondragón", "Mexico"),
    "OMEN": ("3", "Omen", "Unknown", "Unknown"),
    "ISO": ("4", "Iso", "Li Zhao Yu", "China"),
    "FADE": ("5", "Fade", "Hazal Eyletmez", "Turkey"),
    "SOVA": ("6", "Sova", "Sasha Novikov", "Russia"),
    "VIPER": ("7", "Viper", "Sabine Callas", "United States"),
    "KILLJOY": ("8", "Killjoy", "Klara Böhringer", "Germany"),
    "CYPHER": ("9", "Cypher", "Aamir El Amari", "Morocco"),
    "CHAMBER": ("10", "Chamber", "Vincent Fabron", "France")
}

# this function is triggered when search button is pressed
def search_agent(event):
    result_box = document.getElementById('result')
    user_input = document.getElementById('agent_input').value.strip().upper()
    
    # this checks if the input of the user matches w anything in the dictionary
    if user_input in agent_database:
        info = agent_database[user_input]
        result_box.innerHTML = f"""
        <b>Agent Number:</b> {info[0]}<br>
        <b>Agent Name:</b> {info[1]}<br>
        <b>Real Name:</b> {info[2]}<br>
        <b>Origin:</b> {info[3]}
        """
    else:
        # shows the error message if theres nothing or wrong input
        result_box.innerHTML = f"<span style='color: #ff4655;'>'{user_input}' is not found in the database.</span>"