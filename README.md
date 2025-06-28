# ChatDB

ChatDB is an AI-powered conversational agent built using LangChain and OpenAI, designed to understand natural language input and log structured data into a local SQLite database. The application allows users to interact with a database through natural language commands, making data management more intuitive and accessible.

## Features

- **Natural Language Processing**: Interact with the database using conversational language
- **User Management**: Create and retrieve user records with name and age
- **SQLite Database**: Local data storage with automatic table creation
- **AI-Powered Agent**: Uses OpenAI's GPT-3.5-turbo model for intelligent responses
- **Structured Data Validation**: Pydantic models ensure data integrity
- **Interactive CLI**: Simple command-line interface for easy interaction

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package installer)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/zaeemraza6840/ChatDB.git
   cd ChatDB
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv

   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Configuration

1. **Create a `.env` file** in the project root:

   ```bash
   touch .env
   ```

2. **Add your OpenAI API key** to the `.env` file:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   > **Note**: Replace `your_openai_api_key_here` with your actual OpenAI API key. You can get one by signing up at [OpenAI's platform](https://platform.openai.com/).

## Dependencies

The project requires the following packages (add to `requirements.txt` if empty):

```
python-dotenv==1.0.0
langchain==0.1.0
langchain-openai==0.0.5
langchain-core==0.1.0
pydantic==2.5.0
```

## Usage

1. **Start the application**:

   ```bash
   python main.py
   ```

2. **Interact with the agent** using natural language:

   ```
   You: Create a user named John who is 25 years old
   You: Show me all users in the database
   You: Add a new user called Sarah, she's 30
   You: List all users
   ```

3. **Exit the application**:
   ```
   You: q
   ```

## Available Commands

The AI agent can understand various natural language commands:

- **Create users**: "Create a user named [name] who is [age] years old"
- **View users**: "Show me all users", "List all users", "Get all users"
- **Database operations**: "Initialize the database", "Set up the database"

## Project Structure

```
ChatDB/
├── main.py          # Main application entry point
├── service.py       # Database service layer
├── User.py          # User data model
├── requirements.txt # Python dependencies
├── .env            # Environment variables (create this)
└── README.md       # This file
```

## Technical Details

### Database Schema

The application uses SQLite with a simple `users` table:

```sql
CREATE TABLE users (
    name TEXT,
    age INTEGER
);
```

### Key Components

- **`main.py`**: Contains the LangChain agent setup, tools definition, and main interaction loop
- **`service.py`**: Handles database operations (init_db, insert_user, get_all_users)
- **`User.py`**: Pydantic model for user data validation
- **Agent Tools**:
  - `create_user`: Creates new user records
  - `get_all_users`: Retrieves all users from database
  - `init_db`: Initializes the database (if needed)

### AI Model Configuration

- **Model**: GPT-3.5-turbo
- **Temperature**: 0.2 (for consistent responses)
- **Agent Type**: OpenAI Functions Agent
- **Prompt Template**: Uses LangChain Hub's "hwchase17/openai-functions-agent"

## Error Handling

The application includes basic error handling:

- Database connection errors
- Invalid user input validation
- API key authentication errors
- General exception handling

## Development

### Adding New Features

1. **New Database Operations**: Add functions to `service.py`
2. **New Tools**: Create new `@tool` decorated functions in `main.py`
3. **Data Models**: Extend or create new Pydantic models in separate files

### Testing

To test the application:

1. Ensure your `.env` file is properly configured
2. Run the application and try various natural language commands
3. Verify that data is correctly stored in the SQLite database

## Troubleshooting

### Common Issues

1. **"OpenAI API key not found"**: Ensure your `.env` file contains the correct API key
2. **"Module not found"**: Make sure all dependencies are installed via `pip install -r requirements.txt`
3. **"Database errors"**: Check that the application has write permissions in the current directory

### Database Location

The SQLite database (`users.db`) is created in the same directory as the application. You can inspect it directly using SQLite tools:

```bash
sqlite3 users.db
.tables
SELECT * FROM users;
```

## Contribution

write an email to zaeemraza6840@gmail.com if you want to contribute to this project.
