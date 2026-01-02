# YouTube Search Streamlit App

A modern, interactive web application built with Streamlit that allows users to search for YouTube videos and view them in an elegant, responsive interface.

## Features

- **Real-time Search**: Search for any YouTube videos using keywords
- **Embedded Video Player**: View videos directly in the app without auto-play
- **Modern UI**: Beautiful gradient header and card-based layout with smooth hover effects
- **Responsive Design**: 2-column grid layout that adapts to different screen sizes
- **Comprehensive Info**: Display video title, channel, duration, views, and publish date
- **No External CSS**: All styles embedded within the application
- **Fast & Lightweight**: Quick search results with minimal dependencies

## Demo

![App Screenshot](https://via.placeholder.com/800x400?text=YouTube+Search+App)

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Youtube-Search-Streamlit-App
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in the terminal

3. **Start searching**
   - Enter your search query in the text input field
   - Click the "Search" button
   - Browse through the results with embedded video players

## Dependencies

- **streamlit**: Web framework for creating the interactive UI
- **youtube-search**: Python library for searching YouTube videos

## Project Structure

```
Youtube-Search-Streamlit-App/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── LICENSE            # License file
```

## Features Breakdown

### Embedded CSS Styling
- Custom gradient header
- Card-based video layout with hover effects
- Responsive design with smooth transitions
- Professional color scheme and typography

### Video Information Display
- **Title**: Video title with prominent styling
- **Channel**: Creator's channel name
- **Duration**: Video length
- **Views**: View count
- **Publish Time**: When the video was uploaded

### User Experience
- Clean, intuitive interface
- Fast search results (up to 10 videos)
- Embedded YouTube player (no auto-play)
- Direct links to watch on YouTube

## Configuration

You can customize the app by modifying these parameters in `app.py`:

- **Max Results**: Change `max_results=10` in the `search_youtube()` function
- **Layout**: Modify `layout="wide"` in `st.set_page_config()`
- **Columns**: Adjust `st.columns(2)` for different grid layouts
- **CSS Styles**: Update the embedded CSS in `st.markdown()` for custom styling

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Known Issues

- YouTube API rate limits may affect search results
- Some videos may have embedding disabled by the creator
- Search results are limited to public videos only

## Future Enhancements

- [ ] Add filters (duration, upload date, etc.)
- [ ] Implement pagination for more results
- [ ] Add download functionality
- [ ] Include video statistics and analytics
- [ ] Save favorite videos to a playlist
- [ ] Add dark/light theme toggle
- [ ] Implement search history

## Tips

- Use specific keywords for better search results
- Try different search terms to discover more content
- Click the "Watch on YouTube" link to open videos in a new tab

## Contact

For questions, suggestions, or issues, please open an issue in the GitHub repository.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Uses [youtube-search](https://pypi.org/project/youtube-search/) library
- Inspired by modern YouTube UI design

---

Made with love using Streamlit
