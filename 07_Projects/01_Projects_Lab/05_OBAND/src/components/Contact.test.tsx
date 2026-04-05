import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Contact from './Contact';

describe('Contact', () => {
  it('renders section title', () => {
    render(<Contact />);
    expect(screen.getByRole('heading', { level: 2 })).toBeDefined();
  });

  it('renders all contact info', () => {
    render(<Contact />);
    expect(screen.getByText('+1 (470) 595-0121')).toBeDefined();
    expect(screen.getByText('info@oimayen.com')).toBeDefined();
    expect(screen.getByText('Atlanta, Georgia')).toBeDefined();
    expect(screen.getByText('@oimayen')).toBeDefined();
  });

  it('renders form fields', () => {
    render(<Contact />);
    expect(screen.getByLabelText('Nombre Completo *')).toBeDefined();
    expect(screen.getByLabelText('Email *')).toBeDefined();
    expect(screen.getByLabelText('Telefono')).toBeDefined();
    expect(screen.getByLabelText('Empresa')).toBeDefined();
    expect(screen.getByLabelText('Mensaje *')).toBeDefined();
  });

  it('shows validation errors on empty submit', async () => {
    render(<Contact />);
    
    const submitButton = screen.getByRole('button', { name: /Enviar Mensaje/i });
    fireEvent.click(submitButton);
    
    await waitFor(() => {
      expect(screen.getByText('El nombre es requerido')).toBeDefined();
      expect(screen.getByText('El email es requerido')).toBeDefined();
      expect(screen.getByText('El mensaje es requerido')).toBeDefined();
    });
  });

  it('validates email format', async () => {
    render(<Contact />);
    
    // Fill valid name and message so we can test email validation specifically
    fireEvent.change(screen.getByLabelText('Nombre Completo *'), { 
      target: { value: 'John Doe' } 
    });
    fireEvent.change(screen.getByLabelText('Mensaje *'), { 
      target: { value: 'This is a valid test message for the project' } 
    });
    
    // Use a value that fails the custom regex (no dot after @)
    const emailInput = screen.getByLabelText('Email *');
    fireEvent.change(emailInput, { target: { value: 'test@invalid' } });
    
    const submitButton = screen.getByRole('button', { name: /Enviar Mensaje/i });
    fireEvent.click(submitButton);
    
    await waitFor(() => {
      expect(screen.getByText(/Ingresa un email valido/i)).toBeDefined();
    });
  });

  it('submits form with valid data', async () => {
    render(<Contact />);
    
    // Fill form
    fireEvent.change(screen.getByLabelText('Nombre Completo *'), { 
      target: { value: 'John Doe' } 
    });
    fireEvent.change(screen.getByLabelText('Email *'), { 
      target: { value: 'john@example.com' } 
    });
    fireEvent.change(screen.getByLabelText('Mensaje *'), { 
      target: { value: 'Test message for project' } 
    });
    
    const submitButton = screen.getByRole('button', { name: /Enviar Mensaje/i });
    fireEvent.click(submitButton);
    
    await waitFor(() => {
      expect(screen.getByText('Enviando...')).toBeDefined();
    }, { timeout: 100 });
  });
});