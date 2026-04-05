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

// Mock next/image - use a simple functional component wrapper
vi.mock('next/image', () => {
  const MockImage = (props: { src: string; alt: string; [key: string]: unknown }) => {
    const { src, alt, ...rest } = props;
    return React.createElement('img', { src, alt, ...rest });
  };
  return { __esModule: true, default: MockImage };
});