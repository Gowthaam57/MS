import React from "react";
import { Link } from "react-router-dom";
import Navbar from "./Navbar";
import { motion } from "framer-motion";

const variants = {
  visible: { opacity: 1 },
  hidden: { opacity: 0 },
};

const Home = () => {
  return (
    <motion.div
      initial="hidden"
      animate="visible"
      variants={variants}
      transition={{ duration: 1 }}
    >
      <div className="h-screen bg-blue-100">
        <Navbar />
        <div className="h-[90vh] right flex flex-column justify-between align-center md:flex-row ">
          <div className="flex-[0.5] grid grid-row-5 sm:grid-row-8 justify-items-center ">
            <div className="text-4xl h-full font-extrabold row-span-2 columns-1 flex flex-col px-10 sm:px-20 justify-end">
              <p>Empower Yourself</p>
              <p> Change Yourself!</p>
              <p> Join the movement</p>
            </div>
            <div className=" invisible sm:visible w-9/12 -ml-10 mt-10">
              <p className="font-normal text-base">
                <strong>BuzzWomen</strong> is the global movement by and for
                women. We bring transformation within reach. And enable women to
                ignite their personal and collective power. This is our
                invitation to you. We have an unwavering believe in the power
                within women to create change. Our programs are a safe space
                where women empower themselves and change together! Setting in
                place a permanent learning system led and owned by you and your
                fellow women.
              </p>
            </div>
            <div className="w-full px-10 sm:px-20 sm:row-span-2 flex h-full align-top">
              <Link to="/chat">
                <button className="text-white bg-[#fc8803] h-12 w-36 font-medium">
                  Chat with us!
                </button>
              </Link>
            </div>
          </div>
          <div className="invisible md:visible flex-[0.5] h-full clip-your-needful-style">
            <img
              src={
                "https://static.wixstatic.com/media/7d917e_04890c7753a543d284f8259e1b81afb8~mv2.jpg/v1/fill/w_1920,h_1200,al_c/7d917e_04890c7753a543d284f8259e1b81afb8~mv2.jpg"
              }
              alt=""
              className="h-full w-full"
            />
          </div>
        </div>
      </div>
      <div className="h-screen">
        <div className="h-[100vh] right flex flex-column justify-between align-center md:flex-row ">
          <div className="invisible md:visible flex-[0.5] h-full clip-your-needful-style2">
            <img
              src={
                "https://static.wixstatic.com/media/defc8c_aeb6d953a06345229ef86f26fc74c720~mv2.jpg/v1/fill/w_1899,h_681,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/defc8c_aeb6d953a06345229ef86f26fc74c720~mv2.jpg"
              }
              alt=""
              className="object-none h-full"
            />
          </div>
          <div className="flex-[0.5] grid grid-row-5 sm:grid-row-8 justify-items-center ">
            <div className="text-6xl h-full font-extrabold row-span-2 columns-1 flex flex-col px-10 sm:px-20 justify-end">
              <p> India</p>
            </div>
            <div className="invisible sm:visible w-9/12 -ml-10 mt-10">
              <p className="text-xl font-semibold">About</p>
              <p className="font-normal text-base">
                With Buzz Women in India we create a space for women to learn
                and grow together, since 2012. We do this with our mobile
                schools that drive into villages to provide training. We work on
                ‘Self-Shakti’, which means inner-strength, and on how to apply
                this in daily life. Through local Beehives, women groups, a
                permanent learning system is established in every village.
              </p>
            </div>
            <div className="w-full px-10 sm:px-20 sm:row-span-2 flex h-full align-top">
              <Link to="/chat">
                <button className="text-white bg-[#fc8803] h-12 w-36 font-medium">
                  Chat with us!
                </button>
              </Link>
            </div>
          </div>
        </div>
      </div>
      <div className="h-screen bg-blue-100">
        <div className="h-[100vh] right flex flex-column justify-between align-center md:flex-row ">
          <div className="flex-[0.5] grid grid-row-5 sm:grid-row-8 justify-items-center ">
            <div className="text-6xl h-full font-extrabold row-span-2 columns-1 flex flex-col px-10 sm:px-20 justify-end">
              <p> The Gambia</p>
            </div>
            <div className="invisible sm:visible w-9/12 -ml-10 mt-10">
              <p className="text-xl font-semibold">About</p>
              <p className="font-normal text-base">
                With Buzz Women in India we create a space for women to learn
                and grow together, since 2012. We do this with our mobile
                schools that drive into villages to provide training. We work on
                ‘Self-Shakti’, which means inner-strength, and on how to apply
                this in daily life. Through local Beehives, women groups, a
                permanent learning system is established in every village
              </p>
            </div>
            <div className="w-full px-10 sm:px-20 sm:row-span-2 flex h-full align-top">
              <Link to="/chat">
                <button className="text-white bg-[#fc8803] h-12 w-36 font-medium">
                  Chat with us!
                </button>
              </Link>
            </div>
          </div>
          <div className="invisible md:visible flex-[0.5] h-full clip-your-needful-style">
            <img
              src={
                "https://static.wixstatic.com/media/defc8c_5c4d1b6826a44eb1a94c38899eeadcd2~mv2.jpg/v1/fill/w_1899,h_675,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/defc8c_5c4d1b6826a44eb1a94c38899eeadcd2~mv2.jpg"
              }
              alt=""
              className="object-none h-full"
            />
          </div>
        </div>
      </div>
    </motion.div>

    // <div className="h-[100vh] grid grid-column justify-center items-center align-center bg-conic-to-t from-gray-900 via-gray-100 to-gray-900">
    //   <div className="h-3/4 flex-column justify-center align-center items-center ">
    //     <div className="h-2/4 md:text-8xl text-5xl flex gap-2 justify-center align-text-bottom items-end">
    //       <div className="font-normal leading-normal text-purple-800">
    //         Welcome to{" "}
    //       </div>
    //       <div className="font-normal leading-normal text-pink-800">
    //         {" "}
    //         BuzzWomen
    //       </div>
    //     </div>
    //     <Link
    //       to="/chat"
    //       className="flex justify-center align-center items-center p-10"
    //     >
    //       <button className="text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 h-14 w-60 hover:-translate-y-1 hover:scale-110 duration-300">
    //         Chat with us!
    //       </button>
    //     </Link>
    //   </div>
    // </div>
  );
};

export default Home;
