import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [text, setText] = useState('');
    const [avatarParams, setAvatarParams] = useState({});
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleGenerate = async () => {
        setLoading(true);
        try {
            const res = await axios.post('http://localhost:5000/api/generate-avatar', {
                text,
                avatarParams,
            });
            setResponse(res.data);
        } catch (error) {
            setResponse({ error: error.message });
        }
        setLoading(false);
    };

    return (
        <div style={{ maxWidth: 600, margin: 'auto', padding: 20 }}>
            <h1>AI Avatar Generator</h1>
            <div>
                <label>Text to Speak:</label>
                <textarea
                    rows="4"
                    style={{ width: '100%' }}
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
            </div>
            <div style={{ marginTop: 10 }}>
                <button onClick={handleGenerate} disabled={loading || !text}>
                    {loading ? 'Generating...' : 'Generate Avatar'}
                </button>
            </div>
            <div style={{ marginTop: 20 }}>
                {response && (
                    response.error ? (
                        <div style={{ color: 'red' }}>Error: {response.error}</div>
                    ) : (
                        <div>
                            <p>{response.message}</p>
                            <p>Video URL: <a href={response.video_url} target="_blank" rel="noopener noreferrer">{response.video_url}</a></p>
                            <p>Audio URL: <a href={response.audio_url} target="_blank" rel="noopener noreferrer">{response.audio_url}</a></p>
                        </div>
                    )
                )}
            </div>
        </div>
    );
}

export default App;
