import Image from "next/image";
import React from "react";
import Link from "next/link";

type Props = {};

export default function HeroSection({}: Props) {
  const content = {
    // description: "Join us and save lives together",
    cta_button: "Try Now",
    images: {
      a: "/doctor.jpeg",
      b: "/artificial-intelligence-replace-doctor.jpg",
      c: "/doctor1.jpeg",
    },
  };
  return (
    <section className="w-full">
      <div className="mx-auto grid max-w-7xl grid-cols-1 pt-8 md:grid-cols-2">
        {/* Main Content */}
        <div className="flex flex-col space-y-3 py-12">
          <h1 className="flex flex-col space-y-5 text-5xl font-bold text-sky-500">
            <span> For Optimal </span>
            <span>
              <span className="border border-sky-500 text-emerald-500 px-4"> Medical</span> and{" "}
              <span className="border border-sky-500 text-emerald-500">Health </span>{" "}
            </span>
            <span>Care</span>
          </h1>
          {/* <p className="text-lg text-sky-400">{content?.description} </p> */}

          {/* Buttons */}
          <div className="flex flex-row space-x-8 pt-10">
            <Link href="try-now">
              <button className="rounded-md bg-sky-500 px-10 py-3 font-semibold text-white transition hover:bg-sky-700/90 focus:outline-none">
                {content?.cta_button}
              </button>
            </Link>
            {/* <button className="font-semibold text-sky-400 transition hover:text-sky-700 focus:outline-none">
              See more
            </button> */}
          </div>
        </div>
        {/* Images */}
        <div className="relative">
          <div className="absolute left-11 top-1/4 z-10 -mt-2 h-64 w-96">
            <Image
              className=" object-contain "
              src={content?.images?.a}
              fill
              priority
              alt="Doctor a"
            />
          </div>
          <div className="absolute right-1 top-1 z-10 h-[204px] w-[310px]">
            <Image
              className="object-cover"
              src={content?.images?.b}
              fill
              priority
              alt="Doctor b"
            />
          </div>
          <div className="absolute right-1 bottom-1 z-10 h-[175px] w-[310px]">
            <Image
              className="object-cover"
              src={content?.images?.c}
              fill
              priority
              alt="Doctor c"
            />
          </div>
          {/* patterns */}
          <div className="absolute left-60 bottom-0 z-10 flex flex-row">
            <div className="flex flex-col items-end justify-end">
              <div className="h-10 w-10 rounded-full bg-emerald-500"></div>
              <div className="h-20 w-20 rounded-tl-full bg-emerald-500"></div>
            </div>
            <div className="h-20 w-20 rounded-br-full bg-cyan-400"></div>
          </div>
          <div className="absolute right-0 z-0 h-full w-1/2 bg-sky-500"></div>
        </div>
      </div>
    </section>
  );
}
