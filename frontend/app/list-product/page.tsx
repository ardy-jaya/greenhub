"use client";
import React, { useState, useEffect } from "react";
import axios from "axios";
import Image from "next/image";

interface Product {
  product_id: number;
  name: string;
  price: number;
  description: string;
  quantity: number;
  product_category: string;
  product_grade: string;
  product_type: string;
  product_image: string;
}

interface CartItem {
  id: any;
  product_id: Product;
  quantity: number;
}

const ListPage = () => {
  const [products, setProduct] = useState<Product[]>([]);
  const [cart, setCart] = useState<{ id: number, name: string, quantity: number }[]>([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/products/");
        setProduct(response.data);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };
    fetchProducts();

    return () => {
      console.log("Cleanup");
    };
  }, []);

  const addToCart = async (product: Product) => {
    try {
      const response = await fetch("http://127.0.0.1:5000/transaction-details/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          product_id: product.product_id,
          quantity: 1,
          price: product.price       
        }),
      });

      if (response.ok) {
        console.log("Item added to cart");
      } else {
        console.error("Failed to add item to cart");
      }
    } catch (error) {
      console.error("Error adding item to cart:", error);
    }
  };

  return (
    <div>
      <h1>Products</h1>
      <ul>
        {products.map((product) => (
          <div key={product.product_id}>
            <li>{product.name}</li>
            <li>{product.price}</li>
            <li>{product.description}</li>
            <li>{product.quantity}</li>
            <li>{product.product_category}</li>
            <li>{product.product_grade}</li>
            <li>{product.product_type}</li>
            <li>
              <Image
                src={`http://127.0.0.1:5000/uploads/images/${product.product_image}`}
                alt={product.name}
                width={350}
                height={400}
              />
            </li>
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </div>
        ))}
      </ul>
    </div>
  );
};

export default ListPage;
