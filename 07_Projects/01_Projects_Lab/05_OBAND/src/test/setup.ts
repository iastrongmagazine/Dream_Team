import '@testing-library/jest-dom';
import { vi } from 'vitest';
import React from 'react';

// Mock next/navigation for testing
const mockPush = vi.fn();
const mockReplace = vi.fn();
const mockBack = vi.fn();

vi.mock('next/navigation', () => ({
  useRouter: () => ({
    push: mockPush,
    replace: mockReplace,
    back: mockBack,
  }),
  usePathname: () => '/',
}));

// Mock next/image - convert boolean props to strings
vi.mock('next/image', () => {
  const MockImage = (props: { src: string; alt: string; [key: string]: unknown }) => {
    const { src, alt, fill, priority, loading, ...rest } = props;
    const imgProps: Record<string, string> = { src, alt };
    if (fill === true) imgProps.fill = 'true';
    if (priority === true) imgProps.priority = 'true';
    if (loading) imgProps.loading = String(loading);
    return React.createElement('img', { ...imgProps, ...rest });
  };
  return { __esModule: true, default: MockImage };
});

// Mock IntersectionObserver for Framer Motion viewport animations
global.IntersectionObserver = class IntersectionObserver {
  constructor() {}
  disconnect() {}
  observe() {}
  unobserve() {}
  takeRecords() { return []; }
} as unknown as typeof IntersectionObserver;