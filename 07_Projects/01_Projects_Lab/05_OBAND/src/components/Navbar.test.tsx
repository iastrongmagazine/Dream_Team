import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import Navbar from './Navbar';

describe('Navbar', () => {
  it('renders OIM logo', () => {
    render(<Navbar />);
    expect(screen.getByText(/OIM/)).toBeDefined();
  });

  it('renders navigation links', () => {
    render(<Navbar />);
    expect(screen.getByText('Servicios')).toBeDefined();
    expect(screen.getByText('Proyectos')).toBeDefined();
    expect(screen.getByText('Nosotros')).toBeDefined();
    expect(screen.getByText('Contacto')).toBeDefined();
  });

  it('renders CTA button', () => {
    render(<Navbar />);
    expect(screen.getByText('Iniciar Proyecto')).toBeDefined();
  });

  it('toggles mobile menu on button click', () => {
    render(<Navbar />);
    
    // Mobile menu should be hidden initially
    const menuButton = screen.getByLabelText('Toggle menu');
    expect(menuButton).toBeDefined();
    
    // Click to open menu
    fireEvent.click(menuButton);
    
    // Menu should be visible after click
    const mobileMenu = screen.getByLabelText('Menú móvil');
    expect(mobileMenu).toBeDefined();
  });

  it('closes mobile menu when link is clicked', () => {
    render(<Navbar />);
    
    // Open menu
    const menuButton = screen.getByLabelText('Toggle menu');
    fireEvent.click(menuButton);
    
    // Click a nav link in the mobile menu (use first matching - mobile version)
    const serviciosLinks = screen.getAllByText('Servicios');
    const mobileServiciosLink = serviciosLinks[1]; // Mobile menu link is second
    fireEvent.click(mobileServiciosLink);
    
    // Menu should be closed (link clicked triggers close)
    expect(screen.queryByLabelText('Menú móvil')).toBeNull();
  });
});