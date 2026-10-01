import { useState } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [markdown, setMarkdown] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateBlog = async () => {
    if (!topic.trim()) {
      setError("Please enter a topic.");
      return;
    }

    setLoading(true);
    setError("");
    setMarkdown("");

    try {
      const response = await fetch("/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          topic: topic.trim(),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong.");
      }

      setMarkdown(data.markdown);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <main className="container">
        <header>
          <h1>AI Blog Writing Crew</h1>
          <p>
            Enter a topic and let the research, writing, and editing crew
            create a blog post.
          </p>
        </header>

        <section className="generator">
          <label htmlFor="topic">Topic</label>

          <input
            type="text"
            id="topic"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="Enter a topic for your blog post..."
          />

          <button
            onClick={generateBlog}
            disabled={loading}
          >
            {loading ? "Generating..." : "Generate Blog"}
          </button>

          {error && (
            <div className="error">
              {error}
            </div>
          )}
        </section>

        {markdown && (
          <section className="preview">
            <h2>Preview</h2>

            <article className="markdown">
              <ReactMarkdown>{markdown}</ReactMarkdown>
            </article>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;