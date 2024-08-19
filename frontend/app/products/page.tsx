"use client";

import React, { useState } from "react";
import axios from "axios";

const ProductPage = () => {
const [product, setProduct] = useState({
    name: "",
    price: 0,
    description: "",
    stock: 0,
    category: "Standard",
    grade: "",
    type: "",
  });
 
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      try {
        const response = await axios.post("http://127.0.0.1:5000/products/", product);
        console.log("Product created:", response.data);
      } catch (error) {
        console.error("Error creating product:", error);
      }
    };


  return (
    <form className="mt-5" onSubmit={handleSubmit}>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="name">Name</label>
        <input
          type="text"
          className="form-control"
          id="name"
          placeholder="Enter name"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="price">Price</label>
        <input
          type="number"
          className="form-control"
          id="price"
          placeholder="Enter price"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="description">Description</label>
        <textarea
          className="form-control"
          id="description"
          rows={3}
          placeholder="Enter description"
        ></textarea>
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="stock">Stock</label>
        <input
          type="number"
          className="form-control"
          id="stock"
          placeholder="Enter stock"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="category">Category</label>
        <select className="form-control" id="category">
          <option>Standard</option>
          <option>Premium</option>
        </select>
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="grade">Grade</label>
        <input
          type="text"
          className="form-control"
          id="grade"
          placeholder="Enter grade"
        />
      </div>
      <div className="form-group text-center fw-bolder">
        <label htmlFor="type">Type</label>
        <input
          type="text"
          className="form-control"
          id="type"
          placeholder="Enter type"
        />
      </div>
      <div className="mb-3">
        <label htmlFor="formFileSm" className="form-label">Image</label>
        <input className="form-control form-control-sm" id="formFileSm" type="file"/>
      </div>
      
      <div className="text-center">
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </div>
    </form>
  );
};

export default ProductPage;


