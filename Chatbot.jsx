import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

import { motion } from "framer-motion";

const variants = {
  visible: { opacity: 1 },
  hidden: { opacity: 0 },
};

const Chatbot = () => {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([]);

  const [source, setSource] = useState("en");

  const key = "8afbe0d470mshacbe7aba4157758p101e8ajsn182d887c743d";

  //SpeechRecognition
  const [isRecording, setIsRecording] = useState(false);
  const { transcript, resetTranscript, listening } = useSpeechRecognition();

  const start = async (e) => {
    e.preventDefault();
    if (isRecording) {
      SpeechRecognition.stopListening();
      //   console.log(transcript);
      await setMessage(transcript);
      setIsRecording((recording) => !recording);
      console.log("stop listening");
    } else {
      SpeechRecognition.startListening({ continuous: true });
      setIsRecording((recording) => !recording);
      console.log("Listening starts");
    }
  };

  const [language, setLanguage] = useState([
    {
      lang: "English",
      keyword: "en",
    },
    {
      lang: "Kannada",
      keyword: "kn",
    },
    {
      lang: "Bengali",
      keyword: "bn",
    },
    {
      lang: "Hindi",
      keyword: "hi",
    },
    {
      lang: "Tamil",
      keyword: "ta",
    },
    {
      lang: "Telugu",
      keyboard: "te",
    },
    {
      lang: "Malayalam",
      keyword: "ml",
    },
    {
      lang: "Urudu",
      keyword: "ur",
    },
  ]);

  const messageEl = useRef(null);

  const scrollToBottom = () => {
    messageEl.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendClicked = async (e) => {
    console.log("clicked");

    e.preventDefault();

    if (message.length === 0) return;

    //you can use lang detect api here!
    var target = "en";
    var data = message;

    setMessages((messages) => [
      ...messages,
      {
        isSender: true,
        data: data,
      },
    ]);

    // data = "how are you?";
    setMessage("");

    api(data, source, target);
  };

  const api = async (data, source, target) => {
    const encodedParams = new URLSearchParams();
    encodedParams.append("q", data);
    encodedParams.append("target", target);
    encodedParams.append("source", source);

    if (source === "en") {
      replyFromChatBot(data, source, target);
    } else {
      const options = {
        method: "POST",
        url: "https://google-translate1.p.rapidapi.com/language/translate/v2",
        headers: {
          "content-type": "application/x-www-form-urlencoded",
          // "Accept-Encoding": "application/gzip",
          "X-RapidAPI-Key": key,
          "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        },
        data: encodedParams,
      };

      axios
        .request(options)
        .then(function (response) {
          console.log(response.data.data.translations[0].translatedText);
          replyFromChatBot(
            response.data.data.translations[0].translatedText,
            source,
            target
          );
        })
        .catch(function (error) {
          console.error(error);
        });
    }
  };

  const replyFromChatBot = async (data, source, target) => {
    await axios
      .post("http://localhost:5005/webhooks/rest/webhook?format=json", {
        sender: "a",
        message: data,
      })
      .then((res) => {
        console.log("Json object received from bot");
        console.log(res);
        // data = res[0].text;

        res.data.map(async (data) => {
          if (source === "en") {
            setMessages((messages) => [
              ...messages,
              {
                isSender: false,
                data: data.text,
              },
            ]);
          } else {
            console.log("Message to be translated: " + data.text);
            const encodedParams = new URLSearchParams();
            encodedParams.append("q", data.text);
            encodedParams.append("target", source);
            encodedParams.append("source", target);

            const options = {
              method: "POST",
              url: "https://google-translate1.p.rapidapi.com/language/translate/v2",
              headers: {
                "content-type": "application/x-www-form-urlencoded",
                //   "Accept-Encoding": "application/gzip",
                "X-RapidAPI-Key": key,
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
              },
              data: encodedParams,
            };

            axios
              .request(options)
              .then(function (response) {
                console.log(response.data.data.translations[0].translatedText);
                setMessages((messages) => [
                  ...messages,
                  {
                    isSender: false,
                    data: response.data.data.translations[0].translatedText,
                  },
                ]);
              })
              .catch(function (error) {
                console.error(error);
              });
          }
        });
      });

    // return data;
  };
  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={variants}
      transition={{ duration: 1 }}
    >
      <div className="p-3 flex justify-between sm:h-[10vh] h-[20vh] bg-slate-100 rounded-lg px-10 sm:px-20 flex-wrap space-y-7 md:space-y-0">
        <div className="text-4xl font-semibold">
          <Link to="/">
            <strong className="text-[#fc8803] font-semibold">B</strong>uzz
            <strong className="text-[#fc8803] font-semibold">W</strong>omen
          </Link>
        </div>
        <div className="p-1">
          <div className="flex">
            Language Choosen:
            <select
              class="form-select appearance-none
                block
                w-full
                px-3
                py-1.5
                text-base
                font-normal
                text-gray-700
                bg-white bg-clip-padding bg-no-repeat
                border border-solid border-gray-300
                rounded
                transition
                ease-in-out
                m-0
            focus:text-gray-700 focus:bg-white focus:border-[#fc8803] focus:outline-none"
              aria-label="Default select example"
              value={source}
              onChange={(e) => setSource(e.target.value)}
            >
              {language.map((option) => (
                <option value={option.keyword}>{option.lang}</option>
              ))}
              {/* <option selected>Open this select menu</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option> */}
            </select>
          </div>
        </div>
      </div>
      <div className="h-[90vh] flex justify-center items-center px-5 lg:px-12 bg-blue-100    ">
        <div className=" h-4/5 bg-white w-full lg:w-2/5 rounded-2xl flex flex-wrap">
          <div className="h-1/6 bg-[#fc8803] w-full rounded-lg flex justify-center items-center sm:font-medium sm:text-5xl text-xl font-semibold text-white flex-wrap">
            We are here to help you!
          </div>
          <div className=" p-5 h-4/6 min-w-full flex flex-column overflow-scroll gap-3 flex-start flex-wrap">
            {messages.length !== 0 &&
              messages.map((data, key) => (
                <div className="w-full p-2" ref={messageEl} key={key}>
                  <div
                    className={`h-auto p-3 rounded-lg ${
                      !data.isSender
                        ? " bg-gray-100 float-left"
                        : "bg-[#fc8803] text-white float-right"
                    } `}
                  >
                    {data.data}
                  </div>
                </div>
              ))}
          </div>

          <div className="min-w-full rounded-lg px-5 ">
            <form className="flex justify-center items-center">
              <input
                type="text"
                className="flex-grow m-2 py-2 px-4 mr-1 rounded-full border border-gray-300 bg-gray-100 resize-none
         outline-none w-7/12"
                placeholder="Enter your message..."
                value={isRecording ? transcript : message}
                onChange={(e) => setMessage(e.target.value)}
              ></input>
              <div className="" onClick={start}>
                {!listening ? (
                  <button
                    className="bg-orange-500 hover:bg-orange-300 text-white font-bold py-2 px-4 rounded-full"
                    onClick={resetTranscript}
                  >
                    mic
                  </button>
                ) : (
                  <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-full">
                    recording...
                  </button>
                )}
              </div>
              <button
                type="submit"
                className="w-1/12 sm:h-12 sm:w-12 rounded-full  items-center justify-center "
                onClick={(e) => sendClicked(e)}
              >
                <svg
                  class="svg-inline--fa  text-[#fc8803] fa-paper-plane fa-w-10 sm:fa-w-16 sm:w-10 sm:h-10 sm:py-2 sm:mr-2 h-8 w-8 py-1 mr-2 px-1 hover:scale-110"
                  aria-hidden="true"
                  focusable="false"
                  data-prefix="fas"
                  data-icon="paper-plane"
                  role="img"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 512 512"
                >
                  <path
                    fill="currentColor"
                    d="M476 3.2L12.5 270.6c-18.1 10.4-15.8 35.6 2.2 43.2L121 358.4l287.3-253.2c5.5-4.9 13.3 2.6 8.6 8.3L176 407v80.5c0 23.6 28.5 32.9 42.5 15.8L282 426l124.6 52.2c14.2 6 30.4-2.9 33-18.2l72-432C515 7.8 493.3-6.8 476 3.2z"
                  />
                </svg>
              </button>
            </form>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default Chatbot;
