import Chatbot from "./component/Chatbot";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./component/Home";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/chat" element={<Chatbot />} />
      </Routes>
    </Router>
  );
}

export default App;
