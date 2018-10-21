export interface Details {
  name: string;
  location: string;
  twitter: string;
  linkedin: string;
  facebook: string;
  bio: string;
  logo: string;
  website: string;
  founded: number;
  employees: number;
  details: InnerDetails;
  updated: Date;
}

interface InnerDetails {
  industries: Industry[];
  emails: Email[];
  phones: Phone[];
  locations: Location[];
  keywords: string[];
}

interface Industry {
  code: string;
  name: string;
  type: string;
}

interface Email {
  value: string;
  label: string;
}

interface Phone {
  value: string;
  label: string;
}

interface Location {
  addressLine1: string;
  city: string;
  country: string;
}
