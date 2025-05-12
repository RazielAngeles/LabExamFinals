<template>
  <div class="container">
    <h1>Book Management</h1>
    <form @submit.prevent="addBook">
      <input v-model="newBook.title" placeholder="Title" required />
      <input v-model="newBook.author" placeholder="Author" required />
      <input v-model="newBook.isbn" placeholder="ISBN" required type="number" />
      <input v-model.number="newBook.copies_available" type="number" min="1" required />
      <button type="submit" class="primary">Add Book</button>
    </form>
    <div v-if="error" class="error">{{ error }}</div>
    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Author</th>
          <th>ISBN</th>
          <th>Copies</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.isbn }}</td>
          <td>{{ book.copies_available }}</td>
          <td>
            <button class="edit" @click="editBook(book)">Edit</button>
            <button class="delete" @click="deleteBook(book.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
      newBook: { title: '', author: '', isbn: '', copies_available: 1 },
      error: '',
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get('http://localhost:8000/api/books/');
        this.books = response.data;
      } catch (error) {
        this.error = 'Failed to fetch books';
      }
    },
    async addBook() {
      try {
        await axios.post('http://localhost:8000/api/books/', this.newBook);
        this.newBook = { title: '', author: '', isbn: '', copies_available: 1 };
        this.error = '';
        this.fetchBooks();
      } catch (error) {
        this.error = 'Failed to add book';
      }
    },
    async editBook(book) {
      const updatedBook = { ...book };
      const newTitle = prompt('Enter new title:', book.title);
      if (newTitle) {
        updatedBook.title = newTitle;
        try {
          await axios.put(`http://localhost:8000/api/books/${book.id}/`, updatedBook);
          this.error = '';
          this.fetchBooks();
        } catch (error) {
          this.error = 'Failed to update book';
        }
      }
    },
    async deleteBook(id) {
      try {
        await axios.delete(`http://localhost:8000/api/books/${id}/`);
        this.error = '';
        this.fetchBooks();
      } catch (error) {
        this.error = error.response?.data?.error || 'Failed to delete book';
      }
    },
  },
};
</script>