import React, { useState, useEffect } from 'react';

function UploadForm({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:5000/documents/upload', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    onUpload();
    console.log(data);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

function DocumentList() {
  const [documents, setDocuments] = useState([]);

  const fetchDocuments = () => {
    fetch('http://localhost:5000/documents')
      .then(response => response.json())
      .then(data => setDocuments(data));
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return (
    <ul>
      {documents.map(doc => (
        <li key={doc.id}>
          {doc.filename}
          <DownloadButton doc={doc} />
          <DeleteButton doc={doc} onDelete={fetchDocuments} />
        </li>
      ))}
    </ul>
  );
}

function DownloadButton({ doc }) {
  const handleDownload = async () => {
    const response = await fetch(`http://localhost:5000/documents/${doc.id}`);
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = doc.filename;
    a.click();
  };

  return <button onClick={handleDownload}>Download</button>;
}

function DeleteButton({ doc, onDelete }) {
  const handleDelete = async () => {
    await fetch(`http://localhost:5000/documents/${doc.id}`, {
      method: 'DELETE',
    });
    onDelete();
  };

  return <button onClick={handleDelete}>Delete</button>;
}

function App() {
  return (
    <div className="App">
      <h1>Healthcare Document Portal</h1>
      <UploadForm onUpload={() => window.location.reload()} />
      <DocumentList />
    </div>
  );
}

export default App;