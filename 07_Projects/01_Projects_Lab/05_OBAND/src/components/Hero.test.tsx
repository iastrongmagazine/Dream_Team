import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import Hero from './Hero';

describe('Hero', () => {
  it('renders main headline', () => {
    render(<Hero />);
    expect(screen.getByText('Office')).toBeDefined();
    expect(screen.getByText('Installations')).toBeDefined();
    expect(screen.getByText('Mayen')).toBeDefined();
  });

  it('renders tagline badge', () => {
    render(<Hero />);
    expect(screen.getByText('Ingenieria de Espacios')).toBeDefined();
  });

  it('renders description text', () => {
    render(<Hero />);
    expect(screen.getByText(/Expertos en amueblamiento/)).toBeDefined();
  });

  it('renders CTA buttons', () => {
    render(<Hero />);
    expect(screen.getByText('Ver Proyectos')).toBeDefined();
    expect(screen.getByText('Contactar')).toBeDefined();
  });

  it('has correct hrefs on buttons', () => {
    render(<Hero />);
    const verProyectos = screen.getByText('Ver Proyectos').closest('a');
    expect(verProyectos).toHaveAttribute('href', '#proyectos');
    
    const contactar = screen.getByText('Contactar').closest('a');
    expect(contactar).toHaveAttribute('href', '#contacto');
  });
});