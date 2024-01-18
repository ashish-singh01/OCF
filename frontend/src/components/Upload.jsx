import { useState, useEffect } from "react";

export default function Upload() {
  const [file, setFile] = useState(null);
  useEffect(() => {
    // This will log the updated value of 'file' whenever it changes
    console.log(file);
  }, [file]);

  function handleFile(event) {
    setFile(event.target.files[0]);
    console.log(file);
  }

  async function uploadFile() {
    const formData = new FormData();
    formData.append("file", file);

    try {
      await fetch("http://127.0.0.1:5000/upload", {
        mode: "no-cors",
        method: "POST",
        body: formData,
      });
    } catch (error) {
      console.error(error);
    }
    setFile(null);
  }

  return (
    <>
      <input type="file" name="file" onChange={handleFile} />
      <button onClick={uploadFile}>Upload</button>
    </>
  );
}
