import Image from "next/image";
import React from "react";



export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <div className="flex flex-col items-center justify-center w-full">
          <h1 className="text-5xl font-bold text-center text-gray-900">
            Green Hub
          </h1>
          <p className="text-center text-gray-600">
            Green Hub is a sustainable marketing community platform that connects
            eco-friendly businesses. Join to collaborate, share resources, and
            expand your network within the sustainable business ecosystem.
          </p>
        </div>
        <div className="flex flex-col items-center justify-center w-full">
          <Image
            className="w-25 pt-3 z-3"
            src="/3.svg"
            alt="human working with energy plan"
            width={500} // Add appropriate width
            height={500} // Add appropriate height
            
          />
        </div>
      </div>
    </main>
  );
}
