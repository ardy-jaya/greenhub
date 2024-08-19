
import React from "react";
// import "bootstrap/dist/css/bootstrap.min.css";
import { Image } from "react-bootstrap";

const AboutUs: React.FC = () => {
  return (
    <>
      <div
        className="card container text-dark bg-light overlay"
        style={{ marginTop: "20px" }}
      >
        <Image
          src="/4.svg"
          className="card-img w-50"
          style={{ marginLeft: "500px" }}
          alt="sustain line picture"
        />
        <div className="card-img-overlay mt-5 ms-5">
          <h1 className="card-title fs-1 fw-semibold">About Us</h1>
          <p className="card-text fs-3">
            We thrive to become the best community that connects
          </p>
          <p className="card-text fs-3">
            local producers and you. We do it all for our world
          </p>
        </div>

        <Image
          className="w-25 pt-3 z-3"
          src="/3.svg"
          alt="human working with energy plan"
        />
      </div>

      <div className="container mt-5 pb-5">
        <div className="row">
          <div className="col">
            <h1>Our Mission</h1>
            <Image
              src="/4.svg"
              className="card-img w-50 mt-5"
              alt="world mission"
            />
          </div>
          <div className="col">
            <h2>Who we are??</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry
            </p>
            <h2>What We Do</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry
            </p>
            <h2>How to Do</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry 
            </p>
            <h2>What We F</h2>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry
            </p>
          </div>
        </div>
      </div>

      <div className="container">
        <div className="row">
          <h2 className="text-center mb-5">Our Team</h2>
          <div className="col text-center">
            <h3 className="badge rounded-pill text-bg-secondary">Ardy</h3>
            <br />
            <Image src="/7.svg" className="w-100" alt="Ardys Picture" />
          </div>
          <div className="col text-center">
            <h3 className="badge rounded-pill text-bg-secondary text-center">
              Quraisy
            </h3>
            <br />
            <Image src="/8.svg" className="w-100" alt="Widyas Picture" />
          </div>
          <div className="col text-center">
            <h3 className="badge rounded-pill text-bg-secondary">Widya</h3>
            <br />
            <Image src="/9.svg" className="w-100" alt="Quraisy Picture" />
          </div>
        </div>
      </div>
    </>
  );
};
export default AboutUs;
