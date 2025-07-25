This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: apps/v4/content/docs/components/**/*.{md,markdown,rmd,mdx,rst,rest,txt,adoc,asciidoc}
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
apps/
  v4/
    content/
      docs/
        components/
          accordion.mdx
          alert-dialog.mdx
          alert.mdx
          aspect-ratio.mdx
          avatar.mdx
          badge.mdx
          breadcrumb.mdx
          button.mdx
          calendar.mdx
          card.mdx
          carousel.mdx
          chart.mdx
          checkbox.mdx
          collapsible.mdx
          combobox.mdx
          command.mdx
          context-menu.mdx
          data-table.mdx
          date-picker.mdx
          dialog.mdx
          drawer.mdx
          dropdown-menu.mdx
          form.mdx
          hover-card.mdx
          index.mdx
          input-otp.mdx
          input.mdx
          label.mdx
          menubar.mdx
          navigation-menu.mdx
          pagination.mdx
          popover.mdx
          progress.mdx
          radio-group.mdx
          resizable.mdx
          scroll-area.mdx
          select.mdx
          separator.mdx
          sheet.mdx
          sidebar.mdx
          skeleton.mdx
          slider.mdx
          sonner.mdx
          switch.mdx
          table.mdx
          tabs.mdx
          textarea.mdx
          toast.mdx
          toggle-group.mdx
          toggle.mdx
          tooltip.mdx
          typography.mdx
```

# Files

## File: apps/v4/content/docs/components/accordion.mdx
````
---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/accordion
  api: https://www.radix-ui.com/docs/primitives/components/accordion#api-reference
---

<ComponentPreview
  name="accordion-demo"
  className="[&_.preview>[data-orientation=vertical]]:sm:max-w-[80%] **:[.preview]:min-h-[400px]"
  description="An accordion with three items"
  align="start"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add accordion
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-accordion
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="accordion" title="components/ui/accordion.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
```

```tsx showLineNumbers
<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>Is it accessible?</AccordionTrigger>
    <AccordionContent>
      Yes. It adheres to the WAI-ARIA design pattern.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```
````

## File: apps/v4/content/docs/components/alert-dialog.mdx
````
---
title: Alert Dialog
description: A modal dialog that interrupts the user with important content and expects a response.
featured: true
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/alert-dialog
  api: https://www.radix-ui.com/docs/primitives/components/alert-dialog#api-reference
---

<ComponentPreview
  name="alert-dialog-demo"
  title="An alert dialog with cancel and continue buttons."
  description="An alert dialog with cancel and continue buttons."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add alert-dialog
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-alert-dialog
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="alert-dialog" title="components/ui/alert-dialog.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
```

```tsx showLineNumbers
<AlertDialog>
  <AlertDialogTrigger>Open</AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Continue</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```
````

## File: apps/v4/content/docs/components/alert.mdx
````
---
title: Alert
description: Displays a callout for user attention.
component: true
---

<ComponentPreview
  name="alert-demo"
  title="An alert with an icon, title and description."
  description="An alert with an icon, title and description. The title says 'Heads up!' and the description is 'You can add components to your app using the cli.'."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add alert
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="alert" title="components/ui/alert.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
```

```tsx showLineNumbers
<Alert variant="default | destructive">
  <Terminal />
  <AlertTitle>Heads up!</AlertTitle>
  <AlertDescription>
    You can add components and dependencies to your app using the cli.
  </AlertDescription>
</Alert>
```
````

## File: apps/v4/content/docs/components/aspect-ratio.mdx
````
---
title: Aspect Ratio
description: Displays content within a desired ratio.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/aspect-ratio
  api: https://www.radix-ui.com/docs/primitives/components/aspect-ratio#api-reference
---

<ComponentPreview
  name="aspect-ratio-demo"
  title="Aspect Ratio"
  description="A component that displays an image with a 16:9 aspect ratio."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add aspect-ratio
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-aspect-ratio
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="aspect-ratio" title="components/ui/aspect-ratio.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { AspectRatio } from "@/components/ui/aspect-ratio"
```

```tsx showLineNumbers
<AspectRatio ratio={16 / 9}>
  <Image src="..." alt="Image" className="rounded-md object-cover" />
</AspectRatio>
```
````

## File: apps/v4/content/docs/components/avatar.mdx
````
---
title: Avatar
description: An image element with a fallback for representing the user.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/avatar
  api: https://www.radix-ui.com/docs/primitives/components/avatar#api-reference
---

<ComponentPreview
  name="avatar-demo"
  title="Avatar"
  description="An avatar with a fallback."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add avatar
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-avatar
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="avatar" title="components/ui/avatar.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
```

```tsx showLineNumbers
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" />
  <AvatarFallback>CN</AvatarFallback>
</Avatar>
```
````

## File: apps/v4/content/docs/components/badge.mdx
````
---
title: Badge
description: Displays a badge or a component that looks like a badge.
component: true
---

<ComponentPreview
  name="badge-demo"
  title="Badge"
  description="A default badge"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add badge
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="badge" title="components/ui/badge.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Badge } from "@/components/ui/badge"
```

```tsx
<Badge variant="default |outline | secondary | destructive">Badge</Badge>
```

### Link

You can use the `asChild` prop to make another component look like a badge. Here's an example of a link that looks like a badge.

```tsx showLineNumbers
import { Link } from "next/link"

import { Badge } from "@/components/ui/badge"

export function LinkAsBadge() {
  return (
    <Badge asChild>
      <Link href="/">Badge</Link>
    </Badge>
  )
}
```
````

## File: apps/v4/content/docs/components/breadcrumb.mdx
````
---
title: Breadcrumb
description: Displays the path to the current resource using a hierarchy of links.
component: true
---

<ComponentPreview
  name="breadcrumb-demo"
  className="[&_.preview]:p-2"
  description="A breadcrumb with a collapsible dropdown."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add breadcrumb
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="breadcrumb" title="components/ui/breadcrumb.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
```

```tsx showLineNumbers
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbLink href="/components">Components</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

## Examples

### Custom separator

Use a custom component as `children` for `<BreadcrumbSeparator />` to create a custom separator.

<ComponentPreview
  name="breadcrumb-separator"
  description="A breadcrumb with a custom separator"
/>

```tsx showLineNumbers {1,10-12}
import { SlashIcon } from "lucide-react"

...

<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator>
      <SlashIcon />
    </BreadcrumbSeparator>
    <BreadcrumbItem>
      <BreadcrumbLink href="/components">Components</BreadcrumbLink>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

---

### Dropdown

You can compose `<BreadcrumbItem />` with a `<DropdownMenu />` to create a dropdown in the breadcrumb.

<ComponentPreview
  name="breadcrumb-dropdown"
  className="[&_.preview]:p-2"
  description="A breadcrumb with a dropdown."
/>

```tsx showLineNumbers {1-6,11-21}
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

...

<BreadcrumbItem>
  <DropdownMenu>
    <DropdownMenuTrigger>
      Components
    </DropdownMenuTrigger>
    <DropdownMenuContent align="start">
      <DropdownMenuItem>Documentation</DropdownMenuItem>
      <DropdownMenuItem>Themes</DropdownMenuItem>
      <DropdownMenuItem>GitHub</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</BreadcrumbItem>
```

---

### Collapsed

We provide a `<BreadcrumbEllipsis />` component to show a collapsed state when the breadcrumb is too long.

<ComponentPreview
  name="breadcrumb-ellipsis"
  className="[&_.preview]:p-2"
  description="A breadcrumb showing a collapsed state."
/>

```tsx showLineNumbers {1,9}
import { BreadcrumbEllipsis } from "@/components/ui/breadcrumb"

...

<Breadcrumb>
  <BreadcrumbList>
    {/* ... */}
    <BreadcrumbItem>
      <BreadcrumbEllipsis />
    </BreadcrumbItem>
    {/* ... */}
  </BreadcrumbList>
</Breadcrumb>
```

---

### Link component

To use a custom link component from your routing library, you can use the `asChild` prop on `<BreadcrumbLink />`.

<ComponentPreview
  name="breadcrumb-link"
  description="A breadcrumb with a custom Link component"
/>

```tsx showLineNumbers {1,8-10}
import { Link } from "next/link"

...

<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink asChild>
        <Link href="/">Home</Link>
      </BreadcrumbLink>
    </BreadcrumbItem>
    {/* ... */}
  </BreadcrumbList>
</Breadcrumb>
```

---

### Responsive

Here's an example of a responsive breadcrumb that composes `<BreadcrumbItem />` with `<BreadcrumbEllipsis />`, `<DropdownMenu />`, and `<Drawer />`.

It displays a dropdown on desktop and a drawer on mobile.

<ComponentPreview
  name="breadcrumb-responsive"
  className="[&_.preview]:p-2"
  description="A responsive breadcrumb. It displays a dropdown on desktop and a drawer on mobile."
/>
````

## File: apps/v4/content/docs/components/button.mdx
````
---
title: Button
description: Displays a button or a component that looks like a button.
featured: true
component: true
---

<ComponentPreview name="button-demo" description="A button" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add button
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-slot
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="button" title="components/ui/button.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Button } from "@/components/ui/button"
```

```tsx
<Button variant="outline">Button</Button>
```

## Link

You can use the `asChild` prop to make another component look like a button. Here's an example of a link that looks like a button.

```tsx showLineNumbers
import { Link } from "next/link"

import { Button } from "@/components/ui/button"

export function LinkAsButton() {
  return (
    <Button asChild>
      <Link href="/login">Login</Link>
    </Button>
  )
}
```

## Examples

### Default

<ComponentPreview name="button-demo" description="A primary button" />

### Secondary

<ComponentPreview name="button-secondary" description="A secondary button" />

### Destructive

<ComponentPreview
  name="button-destructive"
  description="A destructive button"
/>

### Outline

<ComponentPreview
  name="button-outline"
  description="A button using the outline variant."
/>

### Ghost

<ComponentPreview
  name="button-ghost"
  description="A button using the ghost variant"
/>

### Link

<ComponentPreview
  name="button-link"
  description="A button using the link variant."
/>

### Icon

<ComponentPreview name="button-icon" description="An icon button" />

### With Icon

<ComponentPreview name="button-with-icon" description="A button with an icon" />

### Loading

<ComponentPreview
  name="button-loading"
  description="A button with a loading state."
/>
````

## File: apps/v4/content/docs/components/calendar.mdx
````
---
title: Calendar
description: A date field component that allows users to enter and edit date.
component: true
links:
  doc: https://react-day-picker.js.org
---

<ComponentPreview
  name="calendar-demo"
  title="Calendar"
  description="A calendar showing the current date."
/>

## Blocks

We have built a collection of 30+ calendar blocks that you can use to build your own calendar components.

See all calendar blocks in the [Blocks Library](/blocks/calendar) page.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add calendar
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install react-day-picker date-fns
```

<Step>Add the `Button` component to your project.</Step>

The `Calendar` component uses the `Button` component. Make sure you have it installed in your project.

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="calendar" title="components/ui/calendar.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Calendar } from "@/components/ui/calendar"
```

```tsx showLineNumbers
const [date, setDate] = React.useState<Date | undefined>(new Date())

return (
  <Calendar
    mode="single"
    selected={date}
    onSelect={setDate}
    className="rounded-lg border"
  />
)
```

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.

## About

The `Calendar` component is built on top of [React DayPicker](https://react-day-picker.js.org).

## Customization

See the [React DayPicker](https://react-day-picker.js.org/docs/customization) documentation for more information on how to customize the `Calendar` component.

## Date Picker

You can use the `<Calendar>` component to build a date picker. See the [Date Picker](/docs/components/date-picker) page for more information.

## Persian / Hijri / Jalali Calendar

To use the Persian calendar, edit `components/ui/calendar.tsx` and replace `react-day-picker` with `react-day-picker/persian`.

```diff
- import { DayPicker } from "react-day-picker"
+ import { DayPicker } from "react-day-picker/persian"
```

<ComponentPreview
  name="calendar-hijri"
  title="Persian / Hijri / Jalali Calendar"
  description="A Persian calendar."
/>

## Examples

### Range Calendar

<ComponentPreview
  name="calendar-02"
  title="Range Calendar"
  description="A calendar showing the current date and range selection."
  className="**:[.preview]:h-auto lg:**:[.preview]:h-[450px]"
/>

### Month and Year Selector

<ComponentPreview
  name="calendar-13"
  title="Month and Year Selector"
  description="A calendar with month and year dropdowns."
/>

### Date of Birth Picker

<ComponentPreview
  name="calendar-22"
  title="Date of Birth Picker"
  description="A calendar with date of birth picker."
/>

### Date and Time Picker

<ComponentPreview
  name="calendar-24"
  title="Date and Time Picker"
  description="A calendar with date and time picker."
/>

### Natural Language Picker

This component uses the `chrono-node` library to parse natural language dates.

<ComponentPreview
  name="calendar-29"
  title="Natural Language Picker"
  description="A calendar with natural language picker."
/>

### Form

<ComponentPreview name="calendar-form" />

## Upgrade Guide

### Tailwind v4

If you're already using Tailwind v4, you can upgrade to the latest version of the `Calendar` component by running the following command:

```bash
npx shadcn@latest add calendar
```

When you're prompted to overwrite the existing `Calendar` component, select `Yes`. **If you have made any changes to the `Calendar` component, you will need to merge your changes with the new version.**

This will update the `Calendar` component and `react-day-picker` to the latest version.

Next, follow the [React DayPicker](https://daypicker.dev/upgrading) upgrade guide to upgrade your existing components to the latest version.

#### Installing Blocks

After upgrading the `Calendar` component, you can install the new blocks by running the `shadcn@latest add` command.

```bash
npx shadcn@latest add calendar-02
```

This will install the latest version of the calendar blocks.

### Tailwind v3

If you're using Tailwind v3, you can upgrade to the latest version of the `Calendar` by copying the following code to your `calendar.tsx` file.

<CodeCollapsibleWrapper>

```tsx showLineNumbers title="components/ui/calendar.tsx"
"use client"

import * as React from "react"
import {
  ChevronDownIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
} from "lucide-react"
import { DayButton, DayPicker, getDefaultClassNames } from "react-day-picker"

import { cn } from "@/lib/utils"
import { Button, buttonVariants } from "@/components/ui/button"

function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  captionLayout = "label",
  buttonVariant = "ghost",
  formatters,
  components,
  ...props
}: React.ComponentProps<typeof DayPicker> & {
  buttonVariant?: React.ComponentProps<typeof Button>["variant"]
}) {
  const defaultClassNames = getDefaultClassNames()

  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn(
        "bg-background group/calendar p-3 [--cell-size:2rem] [[data-slot=card-content]_&]:bg-transparent [[data-slot=popover-content]_&]:bg-transparent",
        String.raw`rtl:**:[.rdp-button\_next>svg]:rotate-180`,
        String.raw`rtl:**:[.rdp-button\_previous>svg]:rotate-180`,
        className
      )}
      captionLayout={captionLayout}
      formatters={{
        formatMonthDropdown: (date) =>
          date.toLocaleString("default", { month: "short" }),
        ...formatters,
      }}
      classNames={{
        root: cn("w-fit", defaultClassNames.root),
        months: cn(
          "relative flex flex-col gap-4 md:flex-row",
          defaultClassNames.months
        ),
        month: cn("flex w-full flex-col gap-4", defaultClassNames.month),
        nav: cn(
          "absolute inset-x-0 top-0 flex w-full items-center justify-between gap-1",
          defaultClassNames.nav
        ),
        button_previous: cn(
          buttonVariants({ variant: buttonVariant }),
          "h-[--cell-size] w-[--cell-size] select-none p-0 aria-disabled:opacity-50",
          defaultClassNames.button_previous
        ),
        button_next: cn(
          buttonVariants({ variant: buttonVariant }),
          "h-[--cell-size] w-[--cell-size] select-none p-0 aria-disabled:opacity-50",
          defaultClassNames.button_next
        ),
        month_caption: cn(
          "flex h-[--cell-size] w-full items-center justify-center px-[--cell-size]",
          defaultClassNames.month_caption
        ),
        dropdowns: cn(
          "flex h-[--cell-size] w-full items-center justify-center gap-1.5 text-sm font-medium",
          defaultClassNames.dropdowns
        ),
        dropdown_root: cn(
          "has-focus:border-ring border-input shadow-xs has-focus:ring-ring/50 has-focus:ring-[3px] relative rounded-md border",
          defaultClassNames.dropdown_root
        ),
        dropdown: cn("absolute inset-0 opacity-0", defaultClassNames.dropdown),
        caption_label: cn(
          "select-none font-medium",
          captionLayout === "label"
            ? "text-sm"
            : "[&>svg]:text-muted-foreground flex h-8 items-center gap-1 rounded-md pl-2 pr-1 text-sm [&>svg]:size-3.5",
          defaultClassNames.caption_label
        ),
        table: "w-full border-collapse",
        weekdays: cn("flex", defaultClassNames.weekdays),
        weekday: cn(
          "text-muted-foreground flex-1 select-none rounded-md text-[0.8rem] font-normal",
          defaultClassNames.weekday
        ),
        week: cn("mt-2 flex w-full", defaultClassNames.week),
        week_number_header: cn(
          "w-[--cell-size] select-none",
          defaultClassNames.week_number_header
        ),
        week_number: cn(
          "text-muted-foreground select-none text-[0.8rem]",
          defaultClassNames.week_number
        ),
        day: cn(
          "group/day relative aspect-square h-full w-full select-none p-0 text-center [&:first-child[data-selected=true]_button]:rounded-l-md [&:last-child[data-selected=true]_button]:rounded-r-md",
          defaultClassNames.day
        ),
        range_start: cn(
          "bg-accent rounded-l-md",
          defaultClassNames.range_start
        ),
        range_middle: cn("rounded-none", defaultClassNames.range_middle),
        range_end: cn("bg-accent rounded-r-md", defaultClassNames.range_end),
        today: cn(
          "bg-accent text-accent-foreground rounded-md data-[selected=true]:rounded-none",
          defaultClassNames.today
        ),
        outside: cn(
          "text-muted-foreground aria-selected:text-muted-foreground",
          defaultClassNames.outside
        ),
        disabled: cn(
          "text-muted-foreground opacity-50",
          defaultClassNames.disabled
        ),
        hidden: cn("invisible", defaultClassNames.hidden),
        ...classNames,
      }}
      components={{
        Root: ({ className, rootRef, ...props }) => {
          return (
            <div
              data-slot="calendar"
              ref={rootRef}
              className={cn(className)}
              {...props}
            />
          )
        },
        Chevron: ({ className, orientation, ...props }) => {
          if (orientation === "left") {
            return (
              <ChevronLeftIcon className={cn("size-4", className)} {...props} />
            )
          }

          if (orientation === "right") {
            return (
              <ChevronRightIcon
                className={cn("size-4", className)}
                {...props}
              />
            )
          }

          return (
            <ChevronDownIcon className={cn("size-4", className)} {...props} />
          )
        },
        DayButton: CalendarDayButton,
        WeekNumber: ({ children, ...props }) => {
          return (
            <td {...props}>
              <div className="flex size-[--cell-size] items-center justify-center text-center">
                {children}
              </div>
            </td>
          )
        },
        ...components,
      }}
      {...props}
    />
  )
}

function CalendarDayButton({
  className,
  day,
  modifiers,
  ...props
}: React.ComponentProps<typeof DayButton>) {
  const defaultClassNames = getDefaultClassNames()

  const ref = React.useRef<HTMLButtonElement>(null)
  React.useEffect(() => {
    if (modifiers.focused) ref.current?.focus()
  }, [modifiers.focused])

  return (
    <Button
      ref={ref}
      variant="ghost"
      size="icon"
      data-day={day.date.toLocaleDateString()}
      data-selected-single={
        modifiers.selected &&
        !modifiers.range_start &&
        !modifiers.range_end &&
        !modifiers.range_middle
      }
      data-range-start={modifiers.range_start}
      data-range-end={modifiers.range_end}
      data-range-middle={modifiers.range_middle}
      className={cn(
        "data-[selected-single=true]:bg-primary data-[selected-single=true]:text-primary-foreground data-[range-middle=true]:bg-accent data-[range-middle=true]:text-accent-foreground data-[range-start=true]:bg-primary data-[range-start=true]:text-primary-foreground data-[range-end=true]:bg-primary data-[range-end=true]:text-primary-foreground group-data-[focused=true]/day:border-ring group-data-[focused=true]/day:ring-ring/50 flex aspect-square h-auto w-full min-w-[--cell-size] flex-col gap-1 font-normal leading-none data-[range-end=true]:rounded-md data-[range-middle=true]:rounded-none data-[range-start=true]:rounded-md group-data-[focused=true]/day:relative group-data-[focused=true]/day:z-10 group-data-[focused=true]/day:ring-[3px] [&>span]:text-xs [&>span]:opacity-70",
        defaultClassNames.day,
        className
      )}
      {...props}
    />
  )
}

export { Calendar, CalendarDayButton }
```

</CodeCollapsibleWrapper>

**If you have made any changes to the `Calendar` component, you will need to merge your changes with the new version.**

Then follow the [React DayPicker](https://daypicker.dev/upgrading) upgrade guide to upgrade your dependencies and existing components to the latest version.

#### Installing Blocks

After upgrading the `Calendar` component, you can install the new blocks by running the `shadcn@latest add` command.

```bash
npx shadcn@latest add calendar-02
```

This will install the latest version of the calendar blocks.
````

## File: apps/v4/content/docs/components/card.mdx
````
---
title: Card
description: Displays a card with header, content, and footer.
component: true
---

<ComponentPreview name="card-demo" description="A card with a form" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add card
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="card" title="components/ui/card.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
```

```tsx showLineNumbers
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
    <CardAction>Card Action</CardAction>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
```
````

## File: apps/v4/content/docs/components/carousel.mdx
````
---
title: Carousel
description: A carousel with motion and swipe built using Embla.
component: true
links:
  doc: https://www.embla-carousel.com/get-started/react
  api: https://www.embla-carousel.com/api
---

<ComponentPreview
  name="carousel-demo"
  title="Carousel"
  description="A carousel with 5 items and a previous and next button."
/>

## About

The carousel component is built using the [Embla Carousel](https://www.embla-carousel.com/) library.

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add carousel
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install embla-carousel-react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="carousel" title="components/ui/carousel.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
```

```tsx showLineNumbers
<Carousel>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

## Examples

### Sizes

To set the size of the items, you can use the `basis` utility class on the `<CarouselItem />`.

<ComponentPreview
  name="carousel-size"
  title="Carousel"
  description="A carousel with 3 active items of equal size."
/>

```tsx showLineNumbers {4-6}
// 33% of the carousel width.
<Carousel>
  <CarouselContent>
    <CarouselItem className="basis-1/3">...</CarouselItem>
    <CarouselItem className="basis-1/3">...</CarouselItem>
    <CarouselItem className="basis-1/3">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

```tsx showLineNumbers {4-6}
// 50% on small screens and 33% on larger screens.
<Carousel>
  <CarouselContent>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
    <CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

### Spacing

To set the spacing between the items, we use a `pl-[VALUE]` utility on the `<CarouselItem />` and a negative `-ml-[VALUE]` on the `<CarouselContent />`.

<Callout className="mt-6">
  **Why:** I tried to use the `gap` property or a `grid` layout on the `
  <CarouselContent />` but it required a lot of math and mental effort to get the
  spacing right. I found `pl-[VALUE]` and `-ml-[VALUE]` utilities much easier to
  use.

You can always adjust this in your own project if you need to.

</Callout>

<ComponentPreview
  name="carousel-spacing"
  title="Carousel"
  description="A carousel with 3 items with a spacing of 1rem."
/>

```tsx showLineNumbers /-ml-4/ /pl-4/
<Carousel>
  <CarouselContent className="-ml-4">
    <CarouselItem className="pl-4">...</CarouselItem>
    <CarouselItem className="pl-4">...</CarouselItem>
    <CarouselItem className="pl-4">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

```tsx showLineNumbers /-ml-2/ /pl-2/ /md:-ml-4/ /md:pl-4/
<Carousel>
  <CarouselContent className="-ml-2 md:-ml-4">
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
    <CarouselItem className="pl-2 md:pl-4">...</CarouselItem>
  </CarouselContent>
</Carousel>
```

### Orientation

Use the `orientation` prop to set the orientation of the carousel.

<ComponentPreview
  name="carousel-orientation"
  title="Carousel"
  description="A vertical carousel."
/>

```tsx showLineNumbers /vertical | horizontal/
<Carousel orientation="vertical | horizontal">
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
</Carousel>
```

## Options

You can pass options to the carousel using the `opts` prop. See the [Embla Carousel docs](https://www.embla-carousel.com/api/options/) for more information.

```tsx showLineNumbers {2-5}
<Carousel
  opts={{
    align: "start",
    loop: true,
  }}
>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
</Carousel>
```

## API

Use a state and the `setApi` props to get an instance of the carousel API.

<ComponentPreview
  name="carousel-api"
  title="Carousel"
  description="A carousel with a slide counter."
/>

```tsx showLineNumbers {1,4,22}
import { type CarouselApi } from "@/components/ui/carousel"

export function Example() {
  const [api, setApi] = React.useState<CarouselApi>()
  const [current, setCurrent] = React.useState(0)
  const [count, setCount] = React.useState(0)

  React.useEffect(() => {
    if (!api) {
      return
    }

    setCount(api.scrollSnapList().length)
    setCurrent(api.selectedScrollSnap() + 1)

    api.on("select", () => {
      setCurrent(api.selectedScrollSnap() + 1)
    })
  }, [api])

  return (
    <Carousel setApi={setApi}>
      <CarouselContent>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
      </CarouselContent>
    </Carousel>
  )
}
```

## Events

You can listen to events using the api instance from `setApi`.

```tsx showLineNumbers {1,4-14,16}
import { type CarouselApi } from "@/components/ui/carousel"

export function Example() {
  const [api, setApi] = React.useState<CarouselApi>()

  React.useEffect(() => {
    if (!api) {
      return
    }

    api.on("select", () => {
      // Do something on select.
    })
  }, [api])

  return (
    <Carousel setApi={setApi}>
      <CarouselContent>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
        <CarouselItem>...</CarouselItem>
      </CarouselContent>
    </Carousel>
  )
}
```

See the [Embla Carousel docs](https://www.embla-carousel.com/api/events/) for more information on using events.

## Plugins

You can use the `plugins` prop to add plugins to the carousel.

```ts showLineNumbers {1,6-10}
import Autoplay from "embla-carousel-autoplay"

export function Example() {
  return (
    <Carousel
      plugins={[
        Autoplay({
          delay: 2000,
        }),
      ]}
    >
      // ...
    </Carousel>
  )
}
```

<ComponentPreview
  name="carousel-plugin"
  title="Carousel"
  description="A carousel with the autoplay plugin."
/>

See the [Embla Carousel docs](https://www.embla-carousel.com/api/plugins/) for more information on using plugins.
````

## File: apps/v4/content/docs/components/chart.mdx
````
---
title: Chart
description: Beautiful charts. Built using Recharts. Copy and paste into your apps.
component: true
---

<Callout>

**Note:** We're working on upgrading to Recharts v3. In the meantime, if you'd like to start testing v3, see the code in the comment [here](https://github.com/shadcn-ui/ui/issues/7669#issuecomment-2998299159). We'll have an official release soon.

</Callout>

<ComponentPreview
  name="chart-bar-interactive"
  className="theme-blue [&_.preview]:h-auto [&_.preview]:p-0 [&_.preview]:lg:min-h-[404px] [&_.preview>div]:w-full [&_.preview>div]:border-none [&_.preview>div]:shadow-none"
  hideCode
/>

Introducing **Charts**. A collection of chart components that you can copy and paste into your apps.

Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project.

[Browse the Charts Library](/charts).

## Component

We use [Recharts](https://recharts.org/) under the hood.

We designed the `chart` component with composition in mind. **You build your charts using Recharts components and only bring in custom components, such as `ChartTooltip`, when and where you need it**.

```tsx showLineNumbers /ChartContainer/ /ChartTooltipContent/
import { Bar, BarChart } from "recharts"

import { ChartContainer, ChartTooltipContent } from "@/components/ui/charts"

export function MyChart() {
  return (
    <ChartContainer>
      <BarChart data={data}>
        <Bar dataKey="value" />
        <ChartTooltip content={<ChartTooltipContent />} />
      </BarChart>
    </ChartContainer>
  )
}
```

We do not wrap Recharts. This means you're not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.

**The components are yours**.

## Installation

<Callout className="mt-4">

**Note:** If you are using charts with **React 19** or the **Next.js 15**, see the note [here](/docs/react-19#recharts).

</Callout>

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps>

<Step>Run the following command to install `chart.tsx`</Step>

```bash
npx shadcn@latest add chart
```

<Step>Add the following colors to your CSS file</Step>

```css title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
    --chart-3: oklch(0.398 0.07 227.392);
    --chart-4: oklch(0.828 0.189 84.429);
    --chart-5: oklch(0.769 0.188 70.08);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
    --chart-3: oklch(0.769 0.188 70.08);
    --chart-4: oklch(0.627 0.265 303.9);
    --chart-5: oklch(0.645 0.246 16.439);
  }
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install recharts
```

<Step>Copy and paste the following code into `components/ui/chart.tsx`.</Step>

<ComponentSource name="chart" title="components/ui/chart.tsx" />

<Step>Add the following colors to your CSS file</Step>

```css title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
    --chart-3: oklch(0.398 0.07 227.392);
    --chart-4: oklch(0.828 0.189 84.429);
    --chart-5: oklch(0.769 0.188 70.08);
  }

  .dark {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
    --chart-3: oklch(0.769 0.188 70.08);
    --chart-4: oklch(0.627 0.265 303.9);
    --chart-5: oklch(0.645 0.246 16.439);
  }
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Your First Chart

Let's build your first chart. We'll build a bar chart, add a grid, axis, tooltip and legend.

<Steps>

<Step>Start by defining your data</Step>

The following data represents the number of desktop and mobile users for each month.

<Callout className="mt-4">

**Note:** Your data can be in any shape. You are not limited to the shape of the data below. Use the `dataKey` prop to map your data to the chart.

</Callout>

```tsx title="components/example-chart.tsx" showLineNumbers
const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
  { month: "March", desktop: 237, mobile: 120 },
  { month: "April", desktop: 73, mobile: 190 },
  { month: "May", desktop: 209, mobile: 130 },
  { month: "June", desktop: 214, mobile: 140 },
]
```

<Step>Define your chart config</Step>

The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons and color tokens for theming.

```tsx title="components/example-chart.tsx" showLineNumbers
import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "#60a5fa",
  },
} satisfies ChartConfig
```

<Step>Build your chart</Step>

You can now build your chart using Recharts components.

<Callout className="mt-4 bg-amber-50 border-amber-200 dark:bg-amber-950/50 dark:border-amber-950">

**Important:** Remember to set a `min-h-[VALUE]` on the `ChartContainer` component. This is required for the chart be responsive.

</Callout>

<ComponentSource name="chart-bar-demo" title="components/example-chart.tsx" />

<ComponentPreview
  name="chart-bar-demo"
  className="[&_.preview]:min-h-[250px] [&_.preview]:p-4"
/>

</Steps>

### Add a Grid

Let's add a grid to the chart.

<Steps>

<Step>Import the `CartesianGrid` component.</Step>

```tsx /CartesianGrid/
import { Bar, BarChart, CartesianGrid } from "recharts"
```

<Step>Add the `CartesianGrid` component to your chart.</Step>

```tsx showLineNumbers {3}
<ChartContainer config={chartConfig} className="min-h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  name="chart-bar-demo-grid"
  className="[&_.preview]:min-h-[250px] [&_.preview]:p-4"
/>

</Steps>

### Add an Axis

To add an x-axis to the chart, we'll use the `XAxis` component.

<Steps>

<Step>Import the `XAxis` component.</Step>

```tsx /XAxis/
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
```

<Step>Add the `XAxis` component to your chart.</Step>

```tsx showLineNumbers {4-10}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  name="chart-bar-demo-axis"
  className="[&_.preview]:min-h-[250px] [&_.preview]:p-4"
/>

</Steps>

### Add Tooltip

So far we've only used components from Recharts. They look great out of the box thanks to some customization in the `chart` component.

To add a tooltip, we'll use the custom `ChartTooltip` and `ChartTooltipContent` components from `chart`.

<Steps>

<Step>Import the `ChartTooltip` and `ChartTooltipContent` components.</Step>

```tsx
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

<Step>Add the components to your chart.</Step>

```tsx showLineNumbers {11}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  name="chart-bar-demo-tooltip"
  className="[&_.preview]:min-h-[250px] [&_.preview]:p-4"
/>

Hover to see the tooltips. Easy, right? Two components, and we've got a beautiful tooltip.

</Steps>

### Add Legend

We'll do the same for the legend. We'll use the `ChartLegend` and `ChartLegendContent` components from `chart`.

<Steps>

<Step>Import the `ChartLegend` and `ChartLegendContent` components.</Step>

```tsx
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

<Step>Add the components to your chart.</Step>

```tsx showLineNumbers {12}
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <ChartLegend content={<ChartLegendContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

<ComponentPreview
  name="chart-bar-demo-legend"
  className="[&_.preview]:min-h-[250px] [&_.preview]:p-4"
/>

</Steps>

Done. You've built your first chart! What's next?

- [Themes and Colors](/docs/components/chart#theming)
- [Tooltip](/docs/components/chart#tooltip)
- [Legend](/docs/components/chart#legend)

## Chart Config

The chart config is where you define the labels, icons and colors for a chart.

It is intentionally decoupled from chart data.

This allows you to share config and color tokens between charts. It can also works independently for cases where your data or color tokens live remotely or in a different format.

```tsx showLineNumbers /ChartConfig/
import { Monitor } from "lucide-react"

import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    icon: Monitor,
    // A color like 'hsl(220, 98%, 61%)' or 'var(--color-name)'
    color: "#2563eb",
    // OR a theme object with 'light' and 'dark' keys
    theme: {
      light: "#2563eb",
      dark: "#dc2626",
    },
  },
} satisfies ChartConfig
```

## Theming

Charts has built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl or oklch.

### CSS Variables

<Steps>

<Step>Define your colors in your css file</Step>

```css {6-7,14-15} title="app/globals.css" showLineNumbers
@layer base {
  :root {
    --chart-1: oklch(0.646 0.222 41.116);
    --chart-2: oklch(0.6 0.118 184.704);
  }

  .dark: {
    --chart-1: oklch(0.488 0.243 264.376);
    --chart-2: oklch(0.696 0.17 162.48);
  }
}
```

<Step>Add the color to your `chartConfig`</Step>

```tsx {4,8} showLineNumbers
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

</Steps>

### hex, hsl or oklch

You can also define your colors directly in the chart config. Use the color format you prefer.

```tsx showLineNumbers
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
} satisfies ChartConfig
```

### Using Colors

To use the theme colors in your chart, reference the colors using the format `var(--color-KEY)`.

#### Components

```tsx
<Bar dataKey="desktop" fill="var(--color-desktop)" />
```

#### Chart Data

```tsx showLineNumbers
const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]
```

#### Tailwind

```tsx
<LabelList className="fill-[--color-desktop]" />
```

## Tooltip

A chart tooltip contains a label, name, indicator and value. You can use a combination of these to customize your tooltip.

<ComponentPreview
  name="chart-tooltip-demo"
  className="[&_.preview]:py-0"
  hideCode
/>

You can turn on/off any of these using the `hideLabel`, `hideIndicator` props and customize the indicator style using the `indicator` prop.

Use `labelKey` and `nameKey` to use a custom key for the tooltip label and name.

Chart comes with the `<ChartTooltip>` and `<ChartTooltipContent>` components. You can use these two components to add custom tooltips to your chart.

```tsx
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

```tsx
<ChartTooltip content={<ChartTooltipContent />} />
```

### Props

Use the following props to customize the tooltip.

| Prop            | Type                     | Description                                  |
| :-------------- | :----------------------- | :------------------------------------------- |
| `labelKey`      | string                   | The config or data key to use for the label. |
| `nameKey`       | string                   | The config or data key to use for the name.  |
| `indicator`     | `dot` `line` or `dashed` | The indicator style for the tooltip.         |
| `hideLabel`     | boolean                  | Whether to hide the label.                   |
| `hideIndicator` | boolean                  | Whether to hide the indicator.               |

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for tooltip label and names, use the `labelKey` and `nameKey` props.

```tsx showLineNumbers /browser/
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  visitors: {
    label: "Total Visitors",
  },
  chrome: {
    label: "Chrome",
    color: "hsl(var(--chart-1))",
  },
  safari: {
    label: "Safari",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig
```

```tsx
<ChartTooltip
  content={<ChartTooltipContent labelKey="visitors" nameKey="browser" />}
/>
```

This will use `Total Visitors` for label and `Chrome` and `Safari` for the tooltip names.

## Legend

You can use the custom `<ChartLegend>` and `<ChartLegendContent>` components to add a legend to your chart.

```tsx
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

```tsx
<ChartLegend content={<ChartLegendContent />} />
```

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for legend names, use the `nameKey` prop.

```tsx showLineNumbers /browser/
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  chrome: {
    label: "Chrome",
    color: "hsl(var(--chart-1))",
  },
  safari: {
    label: "Safari",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig
```

```tsx
<ChartLegend content={<ChartLegendContent nameKey="browser" />} />
```

This will use `Chrome` and `Safari` for the legend names.

## Accessibility

You can turn on the `accessibilityLayer` prop to add an accessible layer to your chart.

This prop adds keyboard access and screen reader support to your charts.

```tsx
<LineChart accessibilityLayer />
```
````

## File: apps/v4/content/docs/components/checkbox.mdx
````
---
title: Checkbox
description: A control that allows the user to toggle between checked and not checked.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/checkbox
  api: https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference
---

<ComponentPreview name="checkbox-demo" description="A checkbox" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add checkbox
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-checkbox
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="checkbox" title="components/ui/checkbox.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Checkbox } from "@/components/ui/checkbox"
```

```tsx
<Checkbox />
```

## Examples

### Form

<ComponentPreview name="checkbox-form-multiple" />
````

## File: apps/v4/content/docs/components/collapsible.mdx
````
---
title: Collapsible
description: An interactive component which expands/collapses a panel.
component: true
featured: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/collapsible
  api: https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference
---

<ComponentPreview
  name="collapsible-demo"
  description="A collapsible component."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add collapsible
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-collapsible
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="collapsible" title="components/ui/collapsible.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
```

```tsx showLineNumbers
<Collapsible>
  <CollapsibleTrigger>Can I use this in my project?</CollapsibleTrigger>
  <CollapsibleContent>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </CollapsibleContent>
</Collapsible>
```
````

## File: apps/v4/content/docs/components/combobox.mdx
````
---
title: Combobox
description: Autocomplete input and command palette with a list of suggestions.
component: true
---

<ComponentPreview
  name="combobox-demo"
  description="A combobox with a list of frameworks."
/>

## Installation

The Combobox is built using a composition of the `<Popover />` and the `<Command />` components.

See installation instructions for the [Popover](/docs/components/popover#installation) and the [Command](/docs/components/command#installation) components.

## Usage

<CodeCollapsibleWrapper>

```tsx showLineNumbers title="components/example-combobox.tsx"
"use client"

import * as React from "react"
import { CheckIcon, ChevronsUpDownIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

const frameworks = [
  {
    value: "next.js",
    label: "Next.js",
  },
  {
    value: "sveltekit",
    label: "SvelteKit",
  },
  {
    value: "nuxt.js",
    label: "Nuxt.js",
  },
  {
    value: "remix",
    label: "Remix",
  },
  {
    value: "astro",
    label: "Astro",
  },
]

export function ExampleCombobox() {
  const [open, setOpen] = React.useState(false)
  const [value, setValue] = React.useState("")

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          role="combobox"
          aria-expanded={open}
          className="w-[200px] justify-between"
        >
          {value
            ? frameworks.find((framework) => framework.value === value)?.label
            : "Select framework..."}
          <ChevronsUpDownIcon className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-[200px] p-0">
        <Command>
          <CommandInput placeholder="Search framework..." />
          <CommandList>
            <CommandEmpty>No framework found.</CommandEmpty>
            <CommandGroup>
              {frameworks.map((framework) => (
                <CommandItem
                  key={framework.value}
                  value={framework.value}
                  onSelect={(currentValue) => {
                    setValue(currentValue === value ? "" : currentValue)
                    setOpen(false)
                  }}
                >
                  <CheckIcon
                    className={cn(
                      "mr-2 h-4 w-4",
                      value === framework.value ? "opacity-100" : "opacity-0"
                    )}
                  />
                  {framework.label}
                </CommandItem>
              ))}
            </CommandGroup>
          </CommandList>
        </Command>
      </PopoverContent>
    </Popover>
  )
}
```

</CodeCollapsibleWrapper>

## Examples

### Combobox

<ComponentPreview
  name="combobox-demo"
  description="A combobox with a list of frameworks."
/>

### Popover

<ComponentPreview name="combobox-popover" />

### Dropdown menu

<ComponentPreview
  name="combobox-dropdown-menu"
  description="A combobox in a dropdown menu"
/>

### Responsive

You can create a responsive combobox by using the `<Popover />` on desktop and the `<Drawer />` components on mobile.

<ComponentPreview name="combobox-responsive" />

### Form

<ComponentPreview name="combobox-form" />
````

## File: apps/v4/content/docs/components/command.mdx
````
---
title: Command
description: Fast, composable, unstyled command menu for React.
component: true
links:
  doc: https://cmdk.paco.me
---

<ComponentPreview
  name="command-demo"
  align="start"
  className="[&_.preview>div]:max-w-[450px]"
  description="A command menu"
/>

## About

The `<Command />` component uses the [`cmdk`](https://cmdk.paco.me) component by [pacocoursey](https://twitter.com/pacocoursey).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add command
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install cmdk
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="command" title="components/ui/command.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

```tsx showLineNumbers
<Command>
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
    <CommandSeparator />
    <CommandGroup heading="Settings">
      <CommandItem>Profile</CommandItem>
      <CommandItem>Billing</CommandItem>
      <CommandItem>Settings</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Examples

### Dialog

<ComponentPreview
  name="command-dialog"
  description="A command menu in a dialog"
/>

To show the command menu in a dialog, use the `<CommandDialog />` component.

```tsx showLineNumbers title="components/example-command-menu.tsx"
export function CommandMenu() {
  const [open, setOpen] = React.useState(false)

  React.useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault()
        setOpen((open) => !open)
      }
    }
    document.addEventListener("keydown", down)
    return () => document.removeEventListener("keydown", down)
  }, [])

  return (
    <CommandDialog open={open} onOpenChange={setOpen}>
      <CommandInput placeholder="Type a command or search..." />
      <CommandList>
        <CommandEmpty>No results found.</CommandEmpty>
        <CommandGroup heading="Suggestions">
          <CommandItem>Calendar</CommandItem>
          <CommandItem>Search Emoji</CommandItem>
          <CommandItem>Calculator</CommandItem>
        </CommandGroup>
      </CommandList>
    </CommandDialog>
  )
}
```

### Combobox

You can use the `<Command />` component as a combobox. See the [Combobox](/docs/components/combobox) page for more information.
````

## File: apps/v4/content/docs/components/context-menu.mdx
````
---
title: Context Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/context-menu
  api: https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference
---

<ComponentPreview
  name="context-menu-demo"
  description="A context menu with sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add context-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-context-menu
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="context-menu" title="components/ui/context-menu.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

```tsx showLineNumbers
<ContextMenu>
  <ContextMenuTrigger>Right click</ContextMenuTrigger>
  <ContextMenuContent>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```
````

## File: apps/v4/content/docs/components/data-table.mdx
````
---
title: Data Table
description: Powerful table and datagrids built using TanStack Table.
component: true
links:
  doc: https://tanstack.com/table/v8/docs/introduction
---

<ComponentPreview name="data-table-demo" className="[&_.preview]:items-start" />

## Introduction

Every data table or datagrid I've created has been unique. They all behave differently, have specific sorting and filtering requirements, and work with different data sources.

It doesn't make sense to combine all of these variations into a single component. If we do that, we'll lose the flexibility that [headless UI](https://tanstack.com/table/v8/docs/introduction#what-is-headless-ui) provides.

So instead of a data-table component, I thought it would be more helpful to provide a guide on how to build your own.

We'll start with the basic `<Table />` component and build a complex data table from scratch.

<Callout className="mt-4">

**Tip:** If you find yourself using the same table in multiple places in your app, you can always extract it into a reusable component.

</Callout>

## Table of Contents

This guide will show you how to use [TanStack Table](https://tanstack.com/table) and the `<Table />` component to build your own custom data table. We'll cover the following topics:

- [Basic Table](#basic-table)
- [Row Actions](#row-actions)
- [Pagination](#pagination)
- [Sorting](#sorting)
- [Filtering](#filtering)
- [Visibility](#visibility)
- [Row Selection](#row-selection)
- [Reusable Components](#reusable-components)

## Installation

1. Add the `<Table />` component to your project:

```bash
npx shadcn@latest add table
```

2. Add `tanstack/react-table` dependency:

```bash
npm install @tanstack/react-table
```

## Prerequisites

We are going to build a table to show recent payments. Here's what our data looks like:

```tsx showLineNumbers
type Payment = {
  id: string
  amount: number
  status: "pending" | "processing" | "success" | "failed"
  email: string
}

export const payments: Payment[] = [
  {
    id: "728ed52f",
    amount: 100,
    status: "pending",
    email: "m@example.com",
  },
  {
    id: "489e1d42",
    amount: 125,
    status: "processing",
    email: "example@gmail.com",
  },
  // ...
]
```

## Project Structure

Start by creating the following file structure:

```txt
app
└── payments
    ├── columns.tsx
    ├── data-table.tsx
    └── page.tsx
```

I'm using a Next.js example here but this works for any other React framework.

- `columns.tsx` (client component) will contain our column definitions.
- `data-table.tsx` (client component) will contain our `<DataTable />` component.
- `page.tsx` (server component) is where we'll fetch data and render our table.

## Basic Table

Let's start by building a basic table.

<Steps>

### Column Definitions

First, we'll define our columns.

```tsx showLineNumbers title="app/payments/columns.tsx" {3,14-27}
"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Payment = {
  id: string
  amount: number
  status: "pending" | "processing" | "success" | "failed"
  email: string
}

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "status",
    header: "Status",
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "amount",
    header: "Amount",
  },
]
```

<Callout className="mt-4">

**Note:** Columns are where you define the core of what your table
will look like. They define the data that will be displayed, how it will be
formatted, sorted and filtered.

</Callout>

### `<DataTable />` component

Next, we'll create a `<DataTable />` component to render our table.

```tsx showLineNumbers title="app/payments/data-table.tsx"
"use client"

import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  })

  return (
    <div className="overflow-hidden rounded-md border">
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => {
                return (
                  <TableHead key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </TableHead>
                )
              })}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows?.length ? (
            table.getRowModel().rows.map((row) => (
              <TableRow
                key={row.id}
                data-state={row.getIsSelected() && "selected"}
              >
                {row.getVisibleCells().map((cell) => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))
          ) : (
            <TableRow>
              <TableCell colSpan={columns.length} className="h-24 text-center">
                No results.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
  )
}
```

<Callout>

**Tip**: If you find yourself using `<DataTable />` in multiple places, this is the component you could make reusable by extracting it to `components/ui/data-table.tsx`.

`<DataTable columns={columns} data={data} />`

</Callout>

### Render the table

Finally, we'll render our table in our page component.

```tsx showLineNumbers title="app/payments/page.tsx" {22}
import { columns, Payment } from "./columns"
import { DataTable } from "./data-table"

async function getData(): Promise<Payment[]> {
  // Fetch data from your API here.
  return [
    {
      id: "728ed52f",
      amount: 100,
      status: "pending",
      email: "m@example.com",
    },
    // ...
  ]
}

export default async function DemoPage() {
  const data = await getData()

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  )
}
```

</Steps>

## Cell Formatting

Let's format the amount cell to display the dollar amount. We'll also align the cell to the right.

<Steps>

### Update columns definition

Update the `header` and `cell` definitions for amount as follows:

```tsx showLineNumbers title="app/payments/columns.tsx" {4-15}
export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "amount",
    header: () => <div className="text-right">Amount</div>,
    cell: ({ row }) => {
      const amount = parseFloat(row.getValue("amount"))
      const formatted = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD",
      }).format(amount)

      return <div className="text-right font-medium">{formatted}</div>
    },
  },
]
```

You can use the same approach to format other cells and headers.

</Steps>

## Row Actions

Let's add row actions to our table. We'll use a `<Dropdown />` component for this.

<Steps>

### Update columns definition

Update our columns definition to add a new `actions` column. The `actions` cell returns a `<Dropdown />` component.

```tsx showLineNumbers title="app/payments/columns.tsx" {4,6-14,18-45}
"use client"

import { ColumnDef } from "@tanstack/react-table"
import { MoreHorizontal } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export const columns: ColumnDef<Payment>[] = [
  // ...
  {
    id: "actions",
    cell: ({ row }) => {
      const payment = row.original

      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only">Open menu</span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuLabel>Actions</DropdownMenuLabel>
            <DropdownMenuItem
              onClick={() => navigator.clipboard.writeText(payment.id)}
            >
              Copy payment ID
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem>View customer</DropdownMenuItem>
            <DropdownMenuItem>View payment details</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      )
    },
  },
  // ...
]
```

You can access the row data using `row.original` in the `cell` function. Use this to handle actions for your row eg. use the `id` to make a DELETE call to your API.

</Steps>

## Pagination

Next, we'll add pagination to our table.

<Steps>

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {5,17}
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useReactTable,
} from "@tanstack/react-table"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  // ...
}
```

This will automatically paginate your rows into pages of 10. See the [pagination docs](https://tanstack.com/table/v8/docs/api/features/pagination) for more information on customizing page size and implementing manual pagination.

### Add pagination controls

We can add pagination controls to our table using the `<Button />` component and the `table.previousPage()`, `table.nextPage()` API methods.

```tsx showLineNumbers title="app/payments/data-table.tsx" {1,15,21-39}
import { Button } from "@/components/ui/button"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table>
          { // .... }
        </Table>
      </div>
      <div className="flex items-center justify-end space-x-2 py-4">
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
        >
          Previous
        </Button>
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
        >
          Next
        </Button>
      </div>
    </div>
  )
}
```

See [Reusable Components](#reusable-components) section for a more advanced pagination component.

</Steps>

## Sorting

Let's make the email column sortable.

<Steps>

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" showLineNumbers {3,6,10,18,25-28}
"use client"

import * as React from "react"
import {
  ColumnDef,
  SortingState,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onSortingChange: setSorting,
    getSortedRowModel: getSortedRowModel(),
    state: {
      sorting,
    },
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

### Make header cell sortable

We can now update the `email` header cell to add sorting controls.

```tsx showLineNumbers title="app/payments/columns.tsx" {4,9-19}
"use client"

import { ColumnDef } from "@tanstack/react-table"
import { ArrowUpDown } from "lucide-react"

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "email",
    header: ({ column }) => {
      return (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Email
          <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
      )
    },
  },
]
```

This will automatically sort the table (asc and desc) when the user toggles on the header cell.

</Steps>

## Filtering

Let's add a search input to filter emails in our table.

<Steps>

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {6,10,17,24-26,35-36,39,45-54}
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    onColumnFiltersChange: setColumnFilters,
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      sorting,
      columnFilters,
    },
  })

  return (
    <div>
      <div className="flex items-center py-4">
        <Input
          placeholder="Filter emails..."
          value={(table.getColumn("email")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("email")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
      </div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

Filtering is now enabled for the `email` column. You can add filters to other columns as well. See the [filtering docs](https://tanstack.com/table/v8/docs/guide/filters) for more information on customizing filters.

</Steps>

## Visibility

Adding column visibility is fairly simple using `@tanstack/react-table` visibility API.

<Steps>

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {8,18-23,33-34,45,49,64-91}
"use client"

import * as React from "react"
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({})

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
    },
  })

  return (
    <div>
      <div className="flex items-center py-4">
        <Input
          placeholder="Filter emails..."
          value={table.getColumn("email")?.getFilterValue() as string}
          onChange={(event) =>
            table.getColumn("email")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" className="ml-auto">
              Columns
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table
              .getAllColumns()
              .filter(
                (column) => column.getCanHide()
              )
              .map((column) => {
                return (
                  <DropdownMenuCheckboxItem
                    key={column.id}
                    className="capitalize"
                    checked={column.getIsVisible()}
                    onCheckedChange={(value) =>
                      column.toggleVisibility(!!value)
                    }
                  >
                    {column.id}
                  </DropdownMenuCheckboxItem>
                )
              })}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <div className="overflow-hidden rounded-md border">
        <Table>{ ... }</Table>
      </div>
    </div>
  )
}
```

This adds a dropdown menu that you can use to toggle column visibility.

</Steps>

## Row Selection

Next, we're going to add row selection to our table.

<Steps>

### Update column definitions

```tsx showLineNumbers title="app/payments/columns.tsx" {6,9-27}
"use client"

import { ColumnDef } from "@tanstack/react-table"

import { Badge } from "@/components/ui/badge"
import { Checkbox } from "@/components/ui/checkbox"

export const columns: ColumnDef<Payment>[] = [
  {
    id: "select",
    header: ({ table }) => (
      <Checkbox
        checked={
          table.getIsAllPageRowsSelected() ||
          (table.getIsSomePageRowsSelected() && "indeterminate")
        }
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
        aria-label="Select all"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
        aria-label="Select row"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
]
```

### Update `<DataTable>`

```tsx showLineNumbers title="app/payments/data-table.tsx" {11,23,28}
export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([])
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({})
  const [rowSelection, setRowSelection] = React.useState({})

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
    },
  })

  return (
    <div>
      <div className="overflow-hidden rounded-md border">
        <Table />
      </div>
    </div>
  )
}
```

This adds a checkbox to each row and a checkbox in the header to select all rows.

### Show selected rows

You can show the number of selected rows using the `table.getFilteredSelectedRowModel()` API.

```tsx
<div className="text-muted-foreground flex-1 text-sm">
  {table.getFilteredSelectedRowModel().rows.length} of{" "}
  {table.getFilteredRowModel().rows.length} row(s) selected.
</div>
```

</Steps>

## Reusable Components

Here are some components you can use to build your data tables. This is from the [Tasks](/examples/tasks) demo.

### Column header

Make any column header sortable and hideable.

<ComponentSource
  src="/app/(app)/examples/tasks/components/data-table-column-header.tsx"
  title="components/data-table-column-header.tsx"
/>

```tsx showLineNumbers {5}
export const columns = [
  {
    accessorKey: "email",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Email" />
    ),
  },
]
```

### Pagination

Add pagination controls to your table including page size and selection count.

<ComponentSource src="/app/(app)/examples/tasks/components/data-table-pagination.tsx" />

```tsx
<DataTablePagination table={table} />
```

### Column toggle

A component to toggle column visibility.

<ComponentSource src="/app/(app)/examples/tasks/components/data-table-view-options.tsx" />

```tsx
<DataTableViewOptions table={table} />
```
````

## File: apps/v4/content/docs/components/date-picker.mdx
````
---
title: Date Picker
description: A date picker component with range and presets.
component: true
---

<ComponentPreview
  name="calendar-22"
  title="Date of Birth Picker"
  description="A calendar with date of birth picker."
/>

## Installation

The Date Picker is built using a composition of the `<Popover />` and the `<Calendar />` components.

See installation instructions for the [Popover](/docs/components/popover#installation) and the [Calendar](/docs/components/calendar#installation) components.

## Usage

```tsx showLineNumbers title="components/example-date-picker.tsx"
"use client"

import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function DatePickerDemo() {
  const [date, setDate] = React.useState<Date>()

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          data-empty={!date}
          className="data-[empty=true]:text-muted-foreground w-[280px] justify-start text-left font-normal"
        >
          <CalendarIcon />
          {date ? format(date, "PPP") : <span>Pick a date</span>}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0">
        <Calendar mode="single" selected={date} onSelect={setDate} />
      </PopoverContent>
    </Popover>
  )
}
```

See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.

## Examples

### Date of Birth Picker

<ComponentPreview
  name="calendar-22"
  title="Date of Birth Picker"
  description="A calendar with date of birth picker."
/>

### Picker with Input

<ComponentPreview
  name="calendar-28"
  title="Picker with Input"
  description="A calendar with input and picker."
/>

### Date and Time Picker

<ComponentPreview
  name="calendar-24"
  title="Date and Time Picker"
  description="A calendar with date and time picker."
/>

### Natural Language Picker

This component uses the `chrono-node` library to parse natural language dates.

<ComponentPreview
  name="calendar-29"
  title="Natural Language Picker"
  description="A calendar with natural language picker."
/>

### Form

<ComponentPreview name="date-picker-form" />
````

## File: apps/v4/content/docs/components/dialog.mdx
````
---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
featured: true
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dialog
  api: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
---

<ComponentPreview
  name="dialog-demo"
  description="A dialog for editing profile details."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dialog
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-dialog
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="dialog" title="components/ui/dialog.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
```

```tsx showLineNumbers
<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you absolutely sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

## Examples

### Custom close button

<ComponentPreview name="dialog-close-button" />

## Notes

To use the `Dialog` component from within a `Context Menu` or `Dropdown Menu`, you must encase the `Context Menu` or
`Dropdown Menu` component in the `Dialog` component.

```tsx showLineNumbers title="components/example-dialog-context-menu.tsx" {1, 26}
<Dialog>
  <ContextMenu>
    <ContextMenuTrigger>Right click</ContextMenuTrigger>
    <ContextMenuContent>
      <ContextMenuItem>Open</ContextMenuItem>
      <ContextMenuItem>Download</ContextMenuItem>
      <DialogTrigger asChild>
        <ContextMenuItem>
          <span>Delete</span>
        </ContextMenuItem>
      </DialogTrigger>
    </ContextMenuContent>
  </ContextMenu>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you absolutely sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone. Are you sure you want to permanently
        delete this file from our servers?
      </DialogDescription>
    </DialogHeader>
    <DialogFooter>
      <Button type="submit">Confirm</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```
````

## File: apps/v4/content/docs/components/drawer.mdx
````
---
title: Drawer
description: A drawer component for React.
component: true
links:
  doc: https://vaul.emilkowal.ski/getting-started
---

<ComponentPreview name="drawer-demo" description="A drawer component." />

## About

Drawer is built on top of [Vaul](https://github.com/emilkowalski/vaul) by [emilkowalski\_](https://twitter.com/emilkowalski_).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add drawer
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install vaul
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="drawer" title="components/ui/drawer.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
```

```tsx showLineNumbers
<Drawer>
  <DrawerTrigger>Open</DrawerTrigger>
  <DrawerContent>
    <DrawerHeader>
      <DrawerTitle>Are you absolutely sure?</DrawerTitle>
      <DrawerDescription>This action cannot be undone.</DrawerDescription>
    </DrawerHeader>
    <DrawerFooter>
      <Button>Submit</Button>
      <DrawerClose>
        <Button variant="outline">Cancel</Button>
      </DrawerClose>
    </DrawerFooter>
  </DrawerContent>
</Drawer>
```

## Examples

### Responsive Dialog

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` component on desktop and a `Drawer` on mobile.

<ComponentPreview name="drawer-dialog" />
````

## File: apps/v4/content/docs/components/dropdown-menu.mdx
````
---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
featured: true
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dropdown-menu
  api: https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference
---

<ComponentPreview
  name="dropdown-menu-demo"
  description="A dropdown menu with icons, shortcuts and sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dropdown-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-dropdown-menu
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="dropdown-menu" title="components/ui/dropdown-menu.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

```tsx showLineNumbers
<DropdownMenu>
  <DropdownMenuTrigger>Open</DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuLabel>My Account</DropdownMenuLabel>
    <DropdownMenuSeparator />
    <DropdownMenuItem>Profile</DropdownMenuItem>
    <DropdownMenuItem>Billing</DropdownMenuItem>
    <DropdownMenuItem>Team</DropdownMenuItem>
    <DropdownMenuItem>Subscription</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

## Examples

### Checkboxes

<ComponentPreview
  name="dropdown-menu-checkboxes"
  description="A dropdown menu with checkboxes."
/>

### Radio Group

<ComponentPreview
  name="dropdown-menu-radio-group"
  description="A dropdown menu with radio items."
/>
````

## File: apps/v4/content/docs/components/form.mdx
````
---
title: React Hook Form
description: Building forms with React Hook Form and Zod.
links:
  doc: https://react-hook-form.com
---

Forms are tricky. They are one of the most common things you'll build in a web application, but also one of the most complex.

Well-designed HTML forms are:

- Well-structured and semantically correct.
- Easy to use and navigate (keyboard).
- Accessible with ARIA attributes and proper labels.
- Has support for client and server side validation.
- Well-styled and consistent with the rest of the application.

In this guide, we will take a look at building forms with [`react-hook-form`](https://react-hook-form.com/) and [`zod`](https://zod.dev). We're going to use a `<FormField>` component to compose accessible forms using Radix UI components.

## Features

The `<Form />` component is a wrapper around the `react-hook-form` library. It provides a few things:

- Composable components for building forms.
- A `<FormField />` component for building controlled form fields.
- Form validation using `zod`.
- Handles accessibility and error messages.
- Uses `React.useId()` for generating unique IDs.
- Applies the correct `aria` attributes to form fields based on states.
- Built to work with all Radix UI components.
- Bring your own schema library. We use `zod` but you can use anything you want.
- **You have full control over the markup and styling.**

## Anatomy

```tsx showLineNumbers
<Form>
  <FormField
    control={...}
    name="..."
    render={() => (
      <FormItem>
        <FormLabel />
        <FormControl>
          { /* Your form field */}
        </FormControl>
        <FormDescription />
        <FormMessage />
      </FormItem>
    )}
  />
</Form>
```

## Example

```tsx showLineNumbers
const form = useForm()

<FormField
  control={form.control}
  name="username"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Username</FormLabel>
      <FormControl>
        <Input placeholder="shadcn" {...field} />
      </FormControl>
      <FormDescription>This is your public display name.</FormDescription>
      <FormMessage />
    </FormItem>
  )}
/>
```

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps>

### Command

```bash
npx shadcn@latest add form
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-label @radix-ui/react-slot react-hook-form @hookform/resolvers zod
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="form" title="components/ui/form.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

<Steps>

### Create a form schema

Define the shape of your form using a Zod schema. You can read more about using Zod in the [Zod documentation](https://zod.dev).

```tsx showLineNumbers title="components/example-form.tsx" {3,5-7}
"use client"

import { z } from "zod"

const formSchema = z.object({
  username: z.string().min(2).max(50),
})
```

### Define a form

Use the `useForm` hook from `react-hook-form` to create a form.

```tsx showLineNumbers title="components/example-form.tsx" {3-4,14-20,22-27}
"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
})

export function ProfileForm() {
  // 1. Define your form.
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
    },
  })

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.
    console.log(values)
  }
}
```

Since `FormField` is using a controlled component, you need to provide a default value for the field. See the [React Hook Form docs](https://react-hook-form.com/docs/usecontroller) to learn more about controlled components.

### Build your form

We can now use the `<Form />` components to build our form.

```tsx showLineNumbers title="components/example-form.tsx" {7-17,28-50}
"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"

const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
})

export function ProfileForm() {
  // ...

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="shadcn" {...field} />
              </FormControl>
              <FormDescription>
                This is your public display name.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit">Submit</Button>
      </form>
    </Form>
  )
}
```

### Done

That's it. You now have a fully accessible form that is type-safe with client-side validation.

<ComponentPreview
  name="input-form"
  className="[&_[role=tablist]]:hidden [&>div>div:first-child]:hidden"
/>

</Steps>

## Examples

See the following links for more examples on how to use the `<Form />` component with other components:

- [Checkbox](/docs/components/checkbox#form)
- [Date Picker](/docs/components/date-picker#form)
- [Input](/docs/components/input#form)
- [Radio Group](/docs/components/radio-group#form)
- [Select](/docs/components/select#form)
- [Switch](/docs/components/switch#form)
- [Textarea](/docs/components/textarea#form)
- [Combobox](/docs/components/combobox#form)
````

## File: apps/v4/content/docs/components/hover-card.mdx
````
---
title: Hover Card
description: For sighted users to preview content available behind a link.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/hover-card
  api: https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference
---

<ComponentPreview name="hover-card-demo" description="A hover card component" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add hover-card
```

</TabsContent>

<TabsContent value="manual">

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-hover-card
```

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="hover-card" title="components/ui/hover-card.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
```

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```
````

## File: apps/v4/content/docs/components/index.mdx
````
---
title: Components
description: Here you can find all the components available in the library. We are working on adding more components.
---

<ComponentsList />
````

## File: apps/v4/content/docs/components/input-otp.mdx
````
---
title: Input OTP
description: Accessible one-time password component with copy paste functionality.
component: true
links:
  doc: https://input-otp.rodz.dev
---

<ComponentPreview name="input-otp-demo" description="An 6 digits input OTP." />

## About

Input OTP is built on top of [input-otp](https://github.com/guilhermerodz/input-otp) by [@guilherme_rodz](https://twitter.com/guilherme_rodz).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps>

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add input-otp
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install input-otp
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="input-otp" title="components/ui/input-otp.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"
```

```tsx showLineNumbers
<InputOTP maxLength={6}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
    <InputOTPSlot index={2} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={3} />
    <InputOTPSlot index={4} />
    <InputOTPSlot index={5} />
  </InputOTPGroup>
</InputOTP>
```

## Examples

### Pattern

Use the `pattern` prop to define a custom pattern for the OTP input.

<ComponentPreview
  name="input-otp-pattern"
  description="An input OTP with alphanumeric pattern."
/>

```tsx showLineNumbers {1,7}
import { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp"

...

<InputOTP
  maxLength={6}
  pattern={REGEXP_ONLY_DIGITS_AND_CHARS}
>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    {/* ... */}
  </InputOTPGroup>
</InputOTP>
```

### Separator

You can use the `<InputOTPSeparator />` component to add a separator between the input groups.

<ComponentPreview
  name="input-otp-separator"
  description="An input OTP with custom separator."
/>

```tsx showLineNumbers {4,15}
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"

...

<InputOTP maxLength={4}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={2} />
    <InputOTPSlot index={3} />
  </InputOTPGroup>
</InputOTP>
```

### Controlled

You can use the `value` and `onChange` props to control the input value.

<ComponentPreview name="input-otp-controlled" />

### Form

<ComponentPreview name="input-otp-form" />

## Changelog

### 2024-03-19 Composition

We've made some updates and replaced the render props pattern with composition. Here's how to update your code if you prefer the composition pattern.

<Callout className="mt-6">
  **Note:** You are not required to update your code if you are using the
  `render` prop. It is still supported.
</Callout>

<Steps>

<Step>Update to the latest version of `input-otp`.</Step>

```bash
npm install input-otp@latest
```

<Step>Update `input-otp.tsx`</Step>

```diff showLineNumbers title="input-otp.tsx" {2,8-11}
- import { OTPInput, SlotProps } from "input-otp"
+ import { OTPInput, OTPInputContext } from "input-otp"

 const InputOTPSlot = React.forwardRef<
   React.ElementRef<"div">,
-   SlotProps & React.ComponentPropsWithoutRef<"div">
-  >(({ char, hasFakeCaret, isActive, className, ...props }, ref) => {
+   React.ComponentPropsWithoutRef<"div"> & { index: number }
+  >(({ index, className, ...props }, ref) => {
+   const inputOTPContext = React.useContext(OTPInputContext)
+   const { char, hasFakeCaret, isActive } = inputOTPContext.slots[index]
```

<Step>Then replace the `render` prop in your code.</Step>

```diff showLineNumbers {2-12}
<InputOTP maxLength={6}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
    <InputOTPSlot index={2} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={3} />
    <InputOTPSlot index={4} />
    <InputOTPSlot index={5} />
  </InputOTPGroup>
</InputOTP>
```

</Steps>

### 2024-03-19 Disabled

To add a disabled state to the input, update `<InputOTP />` as follows:

```tsx showLineNumbers title="input-otp.tsx" {4,7-11}
const InputOTP = React.forwardRef<
  React.ElementRef<typeof OTPInput>,
  React.ComponentPropsWithoutRef<typeof OTPInput>
>(({ className, containerClassName, ...props }, ref) => (
  <OTPInput
    ref={ref}
    containerClassName={cn(
      "flex items-center gap-2 has-[:disabled]:opacity-50",
      containerClassName
    )}
    className={cn("disabled:cursor-not-allowed", className)}
    {...props}
  />
))
InputOTP.displayName = "InputOTP"
```
````

## File: apps/v4/content/docs/components/input.mdx
````
---
title: Input
description: Displays a form input field or a component that looks like an input field.
component: true
---

<ComponentPreview
  name="input-demo"
  className="[&_input]:max-w-xs"
  description="A form input component."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add input
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="input" title="components/ui/input.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Input } from "@/components/ui/input"
```

```tsx
<Input />
```

## Examples

### Default

<ComponentPreview
  name="input-demo"
  className="[&_input]:max-w-xs"
  description="A form input component."
/>

### File

<ComponentPreview
  name="input-file"
  className="[&_input]:max-w-xs"
  description="A file input component."
/>

### Disabled

<ComponentPreview
  name="input-disabled"
  className="[&_input]:max-w-xs"
  description="A disabled input component."
/>

### With Label

<ComponentPreview
  name="input-with-label"
  className="[&_input]:max-w-xs"
  description="An input component with a label."
/>

### With Button

<ComponentPreview
  name="input-with-button"
  className="[&_input]:max-w-xs"
  description="An input component with a button."
/>

### Form

<ComponentPreview name="input-form" />
````

## File: apps/v4/content/docs/components/label.mdx
````
---
title: Label
description: Renders an accessible label associated with controls.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/label
  api: https://www.radix-ui.com/docs/primitives/components/label#api-reference
---

<ComponentPreview name="label-demo" description="A label" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add label
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-label
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="label" title="components/ui/label.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Label } from "@/components/ui/label"
```

```tsx
<Label htmlFor="email">Your email address</Label>
```
````

## File: apps/v4/content/docs/components/menubar.mdx
````
---
title: Menubar
description: A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/menubar
  api: https://www.radix-ui.com/docs/primitives/components/menubar#api-reference
---

<ComponentPreview name="menubar-demo" description="A menubar component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add menubar
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-menubar
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="menubar" title="components/ui/menubar.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Menubar,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
```

```tsx showLineNumbers
<Menubar>
  <MenubarMenu>
    <MenubarTrigger>File</MenubarTrigger>
    <MenubarContent>
      <MenubarItem>
        New Tab <MenubarShortcut>⌘T</MenubarShortcut>
      </MenubarItem>
      <MenubarItem>New Window</MenubarItem>
      <MenubarSeparator />
      <MenubarItem>Share</MenubarItem>
      <MenubarSeparator />
      <MenubarItem>Print</MenubarItem>
    </MenubarContent>
  </MenubarMenu>
</Menubar>
```
````

## File: apps/v4/content/docs/components/navigation-menu.mdx
````
---
title: Navigation Menu
description: A collection of links for navigating websites.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/navigation-menu
  api: https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference
---

<ComponentPreview name="navigation-menu-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add navigation-menu
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-navigation-menu
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="navigation-menu"
  title="components/ui/navigation-menu.tsx"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from "@/components/ui/navigation-menu"
```

```tsx showLineNumbers
<NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Item One</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Link</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>
```

## Link

You can use the `asChild` prop to make another component look like a navigation menu trigger. Here's an example of a link that looks like a navigation menu trigger.

```tsx showLineNumbers title="components/example-navigation-menu.tsx"
import { Link } from "next/link"

export function NavigationMenuDemo() {
  return (
    <NavigationMenuItem>
      <NavigationMenuLink asChild>
        <Link href="/docs">Documentation</Link>
      </NavigationMenuLink>
    </NavigationMenuItem>
  )
}
```
````

## File: apps/v4/content/docs/components/pagination.mdx
````
---
title: Pagination
description: Pagination with page navigation, next and previous links.
component: true
---

<ComponentPreview
  name="pagination-demo"
  description="A pagination with previous and next links."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add pagination
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="pagination" title="components/ui/pagination.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
```

```tsx showLineNumbers
<Pagination>
  <PaginationContent>
    <PaginationItem>
      <PaginationPrevious href="#" />
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">1</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationEllipsis />
    </PaginationItem>
    <PaginationItem>
      <PaginationNext href="#" />
    </PaginationItem>
  </PaginationContent>
</Pagination>
```

### Next.js

By default the `<PaginationLink />` component will render an `<a />` tag.

To use the Next.js `<Link />` component, make the following updates to `pagination.tsx`.

```diff showLineNumbers /typeof Link/ {1}
+ import Link from "next/link"

- type PaginationLinkProps = ... & React.ComponentProps<"a">
+ type PaginationLinkProps = ... & React.ComponentProps<typeof Link>

const PaginationLink = ({...props }: ) => (
  <PaginationItem>
-   <a>
+   <Link>
      // ...
-   </a>
+   </Link>
  </PaginationItem>
)

```

<Callout className="mt-6">

**Note:** We are making updates to the cli to automatically do this for you.

</Callout>
````

## File: apps/v4/content/docs/components/popover.mdx
````
---
title: Popover
description: Displays rich content in a portal, triggered by a button.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/popover
  api: https://www.radix-ui.com/docs/primitives/components/popover#api-reference
---

<ComponentPreview
  name="popover-demo"
  description="A popover component with a form."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add popover
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-popover
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="popover" title="components/ui/popover.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
```

```tsx showLineNumbers
<Popover>
  <PopoverTrigger>Open</PopoverTrigger>
  <PopoverContent>Place content for the popover here.</PopoverContent>
</Popover>
```
````

## File: apps/v4/content/docs/components/progress.mdx
````
---
title: Progress
description: Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/progress
  api: https://www.radix-ui.com/docs/primitives/components/progress#api-reference
---

<ComponentPreview
  name="progress-demo"
  description="A progress bar component."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add progress
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-progress
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="progress" title="components/ui/progress.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Progress } from "@/components/ui/progress"
```

```tsx showLineNumbers
<Progress value={33} />
```
````

## File: apps/v4/content/docs/components/radio-group.mdx
````
---
title: Radio Group
description: A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/radio-group
  api: https://www.radix-ui.com/docs/primitives/components/radio-group#api-reference
---

<ComponentPreview
  name="radio-group-demo"
  description="A radio group with 3 items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add radio-group
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-radio-group
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="radio-group" title="components/ui/radio-group.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
```

```tsx showLineNumbers
<RadioGroup defaultValue="option-one">
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="option-one" id="option-one" />
    <Label htmlFor="option-one">Option One</Label>
  </div>
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="option-two" id="option-two" />
    <Label htmlFor="option-two">Option Two</Label>
  </div>
</RadioGroup>
```

## Examples

### Form

<ComponentPreview name="radio-group-form" />
````

## File: apps/v4/content/docs/components/resizable.mdx
````
---
title: Resizable
description: Accessible resizable panel groups and layouts with keyboard support.
component: true
links:
  doc: https://github.com/bvaughn/react-resizable-panels
  api: https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels
---

<ComponentPreview
  name="resizable-demo"
  description="A group of resizable horizontal and vertical panels."
/>

## About

The `Resizable` component is built on top of [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) by [bvaughn](https://github.com/bvaughn).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add resizable
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install react-resizable-panels
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="resizable" title="components/ui/resizable.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
```

```tsx showLineNumbers
<ResizablePanelGroup direction="horizontal">
  <ResizablePanel>One</ResizablePanel>
  <ResizableHandle />
  <ResizablePanel>Two</ResizablePanel>
</ResizablePanelGroup>
```

## Examples

### Vertical

Use the `direction` prop to set the direction of the resizable panels.

<ComponentPreview
  name="resizable-vertical"
  description="A group of resizable vertical panels."
/>

```tsx showLineNumbers {9}
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

export default function Example() {
  return (
    <ResizablePanelGroup direction="vertical">
      <ResizablePanel>One</ResizablePanel>
      <ResizableHandle />
      <ResizablePanel>Two</ResizablePanel>
    </ResizablePanelGroup>
  )
}
```

### Handle

You can set or hide the handle by using the `withHandle` prop on the `ResizableHandle` component.

<ComponentPreview
  name="resizable-handle"
  description="A group of resizable panels with a handle."
/>

```tsx showLineNumbers {11}
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"

export default function Example() {
  return (
    <ResizablePanelGroup direction="horizontal">
      <ResizablePanel>One</ResizablePanel>
      <ResizableHandle withHandle />
      <ResizablePanel>Two</ResizablePanel>
    </ResizablePanelGroup>
  )
}
```
````

## File: apps/v4/content/docs/components/scroll-area.mdx
````
---
title: Scroll-area
description: Augments native scroll functionality for custom, cross-browser styling.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/scroll-area
  api: https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference
---

<ComponentPreview
  name="scroll-area-demo"
  description="A scroll area component."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add scroll-area
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-scroll-area
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="scroll-area" title="components/ui/scroll-area.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { ScrollArea } from "@/components/ui/scroll-area"
```

```tsx showLineNumbers
<ScrollArea className="h-[200px] w-[350px] rounded-md border p-4">
  Jokester began sneaking into the castle in the middle of the night and leaving
  jokes all over the place: under the king's pillow, in his soup, even in the
  royal toilet. The king was furious, but he couldn't seem to stop Jokester. And
  then, one day, the people of the kingdom discovered that the jokes left by
  Jokester were so funny that they couldn't help but laugh. And once they
  started laughing, they couldn't stop.
</ScrollArea>
```

## Examples

### Horizontal Scrolling

<ComponentPreview name="scroll-area-horizontal-demo" />
````

## File: apps/v4/content/docs/components/select.mdx
````
---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
component: true
featured: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/select
  api: https://www.radix-ui.com/docs/primitives/components/select#api-reference
---

<ComponentPreview
  name="select-demo"
  description="A select component with a list of options."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add select
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-select
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="select" title="components/ui/select.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

```tsx showLineNumbers
<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="light">Light</SelectItem>
    <SelectItem value="dark">Dark</SelectItem>
    <SelectItem value="system">System</SelectItem>
  </SelectContent>
</Select>
```

## Examples

### Scrollable

<ComponentPreview
  name="select-scrollable"
  description="A select component with a scrollable list of options."
/>

### Form

<ComponentPreview name="select-form" />
````

## File: apps/v4/content/docs/components/separator.mdx
````
---
title: Separator
description: Visually or semantically separates content.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/separator
  api: https://www.radix-ui.com/docs/primitives/components/separator#api-reference
---

<ComponentPreview name="separator-demo" description="A separator component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add separator
```

</TabsContent>

<TabsContent value="manual">

<Steps>
<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-separator
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="separator" title="components/ui/separator.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Separator } from "@/components/ui/separator"
```

```tsx showLineNumbers
<Separator />
```
````

## File: apps/v4/content/docs/components/sheet.mdx
````
---
title: Sheet
description: Extends the Dialog component to display content that complements the main content of the screen.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dialog
  api: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
---

<ComponentPreview name="sheet-demo" description="A sheet component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add sheet
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-dialog
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="sheet" title="components/ui/sheet.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

### Usage

```tsx showLineNumbers
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
```

```tsx showLineNumbers
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Are you absolutely sure?</SheetTitle>
      <SheetDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```

## Examples

### Side

Use the `side` property to `<SheetContent />` to indicate the edge of the screen where the component will appear. The values can be `top`, `right`, `bottom` or `left`.

### Size

You can adjust the size of the sheet using CSS classes:

```tsx showLineNumbers {3}
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent className="w-[400px] sm:w-[540px]">
    <SheetHeader>
      <SheetTitle>Are you absolutely sure?</SheetTitle>
      <SheetDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```
````

## File: apps/v4/content/docs/components/sidebar.mdx
````
---
title: Sidebar
description: A composable, themeable and customizable sidebar component.
component: true
---

<figure className="flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-07"
    title="Sidebar"
    type="block"
    description="A composable, themeable and customizable sidebar component built using shadcn/ui"
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar that collapses to icons.
  </figcaption>
</figure>

Sidebars are one of the most complex components to build. They are central
to any application and often contain a lot of moving parts.

I don't like building sidebars. So I built 30+ of them. All kinds of
configurations. Then I extracted the core components into `sidebar.tsx`.

We now have a solid foundation to build on top of. Composable. Themeable.
Customizable.

[Browse the Blocks Library](/blocks).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps>

<Step>Run the following command to install `sidebar.tsx`</Step>

```bash
npx shadcn@latest add sidebar
```

<Step>Add the following colors to your CSS file</Step>

The command above should install the colors for you. If not, copy and paste the following in your CSS file.

We'll go over the colors later in the [theming section](/docs/components/sidebar#theming).

```css showLineNumbers title="app/globals.css"
@layer base {
  :root {
    --sidebar: oklch(0.985 0 0);
    --sidebar-foreground: oklch(0.145 0 0);
    --sidebar-primary: oklch(0.205 0 0);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.97 0 0);
    --sidebar-accent-foreground: oklch(0.205 0 0);
    --sidebar-border: oklch(0.922 0 0);
    --sidebar-ring: oklch(0.708 0 0);
  }

  .dark {
    --sidebar: oklch(0.205 0 0);
    --sidebar-foreground: oklch(0.985 0 0);
    --sidebar-primary: oklch(0.488 0.243 264.376);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.269 0 0);
    --sidebar-accent-foreground: oklch(0.985 0 0);
    --sidebar-border: oklch(1 0 0 / 10%);
    --sidebar-ring: oklch(0.439 0 0);
  }
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="sidebar" title="components/ui/sidebar.tsx" />

<Step>Update the import paths to match your project setup.</Step>

<Step>Add the following colors to your CSS file</Step>

We'll go over the colors later in the [theming section](/docs/components/sidebar#theming).

```css showLineNumbers title="app/globals.css"
@layer base {
  :root {
    --sidebar: oklch(0.985 0 0);
    --sidebar-foreground: oklch(0.145 0 0);
    --sidebar-primary: oklch(0.205 0 0);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.97 0 0);
    --sidebar-accent-foreground: oklch(0.205 0 0);
    --sidebar-border: oklch(0.922 0 0);
    --sidebar-ring: oklch(0.708 0 0);
  }

  .dark {
    --sidebar: oklch(0.205 0 0);
    --sidebar-foreground: oklch(0.985 0 0);
    --sidebar-primary: oklch(0.488 0.243 264.376);
    --sidebar-primary-foreground: oklch(0.985 0 0);
    --sidebar-accent: oklch(0.269 0 0);
    --sidebar-accent-foreground: oklch(0.985 0 0);
    --sidebar-border: oklch(1 0 0 / 10%);
    --sidebar-ring: oklch(0.439 0 0);
  }
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Structure

A `Sidebar` component is composed of the following parts:

- `SidebarProvider` - Handles collapsible state.
- `Sidebar` - The sidebar container.
- `SidebarHeader` and `SidebarFooter` - Sticky at the top and bottom of the sidebar.
- `SidebarContent` - Scrollable content.
- `SidebarGroup` - Section within the `SidebarContent`.
- `SidebarTrigger` - Trigger for the `Sidebar`.

<Image
  src="/images/sidebar-structure.png"
  width="716"
  height="420"
  alt="Sidebar Structure"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/sidebar-structure-dark.png"
  width="716"
  height="420"
  alt="Sidebar Structure"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border dark:block"
/>

## Usage

```tsx showLineNumbers title="app/layout.tsx"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

```tsx showLineNumbers title="components/app-sidebar.tsx"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
} from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader />
      <SidebarContent>
        <SidebarGroup />
        <SidebarGroup />
      </SidebarContent>
      <SidebarFooter />
    </Sidebar>
  )
}
```

## Your First Sidebar

Let's start with the most basic sidebar. A collapsible sidebar with a menu.

<Steps>

<Step>
  Add a `SidebarProvider` and `SidebarTrigger` at the root of your application.
</Step>

```tsx showLineNumbers title="app/layout.tsx"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

<Step>Create a new sidebar component at `components/app-sidebar.tsx`.</Step>

```tsx showLineNumbers title="components/app-sidebar.tsx"
import { Sidebar, SidebarContent } from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarContent />
    </Sidebar>
  )
}
```

<Step>Now, let's add a `SidebarMenu` to the sidebar.</Step>

We'll use the `SidebarMenu` component in a `SidebarGroup`.

```tsx showLineNumbers title="components/app-sidebar.tsx"
import { Calendar, Home, Inbox, Search, Settings } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"

// Menu items.
const items = [
  {
    title: "Home",
    url: "#",
    icon: Home,
  },
  {
    title: "Inbox",
    url: "#",
    icon: Inbox,
  },
  {
    title: "Calendar",
    url: "#",
    icon: Calendar,
  },
  {
    title: "Search",
    url: "#",
    icon: Search,
  },
  {
    title: "Settings",
    url: "#",
    icon: Settings,
  },
]

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  )
}
```

<Step>You've created your first sidebar.</Step>

You should see something like this:

<figure className="flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-demo"
    title="Sidebar"
    type="block"
    description="Your first sidebar."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    Your first sidebar.
  </figcaption>
</figure>

</Steps>

## Components

The components in `sidebar.tsx` are built to be composable i.e you build your sidebar by putting the provided components together. They also compose well with other shadcn/ui components such as `DropdownMenu`, `Collapsible` or `Dialog` etc.

**If you need to change the code in `sidebar.tsx`, you are encouraged to do so. The code is yours. Use `sidebar.tsx` as a starting point and build your own.**

In the next sections, we'll go over each component and how to use them.

## SidebarProvider

The `SidebarProvider` component is used to provide the sidebar context to the `Sidebar` component. You should always wrap your application in a `SidebarProvider` component.

### Props

| Name           | Type                      | Description                                  |
| -------------- | ------------------------- | -------------------------------------------- |
| `defaultOpen`  | `boolean`                 | Default open state of the sidebar.           |
| `open`         | `boolean`                 | Open state of the sidebar (controlled).      |
| `onOpenChange` | `(open: boolean) => void` | Sets open state of the sidebar (controlled). |

### Width

If you have a single sidebar in your application, you can use the `SIDEBAR_WIDTH` and `SIDEBAR_WIDTH_MOBILE` variables in `sidebar.tsx` to set the width of the sidebar.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
```

For multiple sidebars in your application, you can use the `style` prop to set the width of the sidebar.

To set the width of the sidebar, you can use the `--sidebar-width` and `--sidebar-width-mobile` CSS variables in the `style` prop.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
<SidebarProvider
  style={{
    "--sidebar-width": "20rem",
    "--sidebar-width-mobile": "20rem",
  }}
>
  <Sidebar />
</SidebarProvider>
```

This will handle the width of the sidebar but also the layout spacing.

### Keyboard Shortcut

The `SIDEBAR_KEYBOARD_SHORTCUT` variable is used to set the keyboard shortcut used to open and close the sidebar.

To trigger the sidebar, you use the `cmd+b` keyboard shortcut on Mac and `ctrl+b` on Windows.

You can change the keyboard shortcut by updating the `SIDEBAR_KEYBOARD_SHORTCUT` variable.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"
```

### Persisted State

The `SidebarProvider` supports persisting the sidebar state across page reloads and server-side rendering. It uses cookies to store the current state of the sidebar. When the sidebar state changes, a default cookie named `sidebar_state` is set with the current open/closed state. This cookie is then read on subsequent page loads to restore the sidebar state.

To persist sidebar state in Next.js, set up your `SidebarProvider` in `app/layout.tsx` like this:

```tsx showLineNumbers title="app/layout.tsx"
import { cookies } from "next/headers"

import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

export async function Layout({ children }: { children: React.ReactNode }) {
  const cookieStore = await cookies()
  const defaultOpen = cookieStore.get("sidebar_state")?.value === "true"

  return (
    <SidebarProvider defaultOpen={defaultOpen}>
      <AppSidebar />
      <main>
        <SidebarTrigger />
        {children}
      </main>
    </SidebarProvider>
  )
}
```

You can change the name of the cookie by updating the `SIDEBAR_COOKIE_NAME` variable in `sidebar.tsx`.

```tsx showLineNumbers title="components/ui/sidebar.tsx"
const SIDEBAR_COOKIE_NAME = "sidebar_state"
```

## Sidebar

The main `Sidebar` component used to render a collapsible sidebar.

```tsx showLineNumbers
import { Sidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  return <Sidebar />
}
```

### Props

| Property      | Type                              | Description                       |
| ------------- | --------------------------------- | --------------------------------- |
| `side`        | `left` or `right`                 | The side of the sidebar.          |
| `variant`     | `sidebar`, `floating`, or `inset` | The variant of the sidebar.       |
| `collapsible` | `offcanvas`, `icon`, or `none`    | Collapsible state of the sidebar. |

### side

Use the `side` prop to change the side of the sidebar.

Available options are `left` and `right`.

```tsx showLineNumbers
import { Sidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  return <Sidebar side="left | right" />
}
```

### variant

Use the `variant` prop to change the variant of the sidebar.

Available options are `sidebar`, `floating` and `inset`.

```tsx showLineNumbers
import { Sidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  return <Sidebar variant="sidebar | floating | inset" />
}
```

<Callout>
  **Note:** If you use the `inset` variant, remember to wrap your main content
  in a `SidebarInset` component.
</Callout>

```tsx showLineNumbers
<SidebarProvider>
  <Sidebar variant="inset" />
  <SidebarInset>
    <main>{children}</main>
  </SidebarInset>
</SidebarProvider>
```

### collapsible

Use the `collapsible` prop to make the sidebar collapsible.

Available options are `offcanvas`, `icon` and `none`.

```tsx showLineNumbers
import { Sidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  return <Sidebar collapsible="offcanvas | icon | none" />
}
```

| Prop        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `offcanvas` | A collapsible sidebar that slides in from the left or right. |
| `icon`      | A sidebar that collapses to icons.                           |
| `none`      | A non-collapsible sidebar.                                   |

## useSidebar

The `useSidebar` hook is used to control the sidebar.

```tsx showLineNumbers
import { useSidebar } from "@/components/ui/sidebar"

export function AppSidebar() {
  const {
    state,
    open,
    setOpen,
    openMobile,
    setOpenMobile,
    isMobile,
    toggleSidebar,
  } = useSidebar()
}
```

| Property        | Type                      | Description                                   |
| --------------- | ------------------------- | --------------------------------------------- |
| `state`         | `expanded` or `collapsed` | The current state of the sidebar.             |
| `open`          | `boolean`                 | Whether the sidebar is open.                  |
| `setOpen`       | `(open: boolean) => void` | Sets the open state of the sidebar.           |
| `openMobile`    | `boolean`                 | Whether the sidebar is open on mobile.        |
| `setOpenMobile` | `(open: boolean) => void` | Sets the open state of the sidebar on mobile. |
| `isMobile`      | `boolean`                 | Whether the sidebar is on mobile.             |
| `toggleSidebar` | `() => void`              | Toggles the sidebar. Desktop and mobile.      |

## SidebarHeader

Use the `SidebarHeader` component to add a sticky header to the sidebar.

The following example adds a `<DropdownMenu>` to the `SidebarHeader`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-header"
    title="Sidebar"
    type="block"
    description="A sidebar header with a dropdown menu."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar header with a dropdown menu.
  </figcaption>
</figure>

```tsx showLineNumbers title="components/app-sidebar.tsx"
<Sidebar>
  <SidebarHeader>
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton>
              Select Workspace
              <ChevronDown className="ml-auto" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-[--radix-popper-anchor-width]">
            <DropdownMenuItem>
              <span>Acme Inc</span>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <span>Acme Corp.</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  </SidebarHeader>
</Sidebar>
```

## SidebarFooter

Use the `SidebarFooter` component to add a sticky footer to the sidebar.

The following example adds a `<DropdownMenu>` to the `SidebarFooter`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-footer"
    title="Sidebar"
    type="block"
    description="A sidebar footer with a dropdown menu."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar footer with a dropdown menu.
  </figcaption>
</figure>

```tsx showLineNumbers title="components/app-sidebar.tsx"
export function AppSidebar() {
  return (
    <SidebarProvider>
      <Sidebar>
        <SidebarHeader />
        <SidebarContent />
        <SidebarFooter>
          <SidebarMenu>
            <SidebarMenuItem>
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <SidebarMenuButton>
                    <User2 /> Username
                    <ChevronUp className="ml-auto" />
                  </SidebarMenuButton>
                </DropdownMenuTrigger>
                <DropdownMenuContent
                  side="top"
                  className="w-[--radix-popper-anchor-width]"
                >
                  <DropdownMenuItem>
                    <span>Account</span>
                  </DropdownMenuItem>
                  <DropdownMenuItem>
                    <span>Billing</span>
                  </DropdownMenuItem>
                  <DropdownMenuItem>
                    <span>Sign out</span>
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarFooter>
      </Sidebar>
    </SidebarProvider>
  )
}
```

## SidebarContent

The `SidebarContent` component is used to wrap the content of the sidebar. This is where you add your `SidebarGroup` components. It is scrollable.

```tsx showLineNumbers
import { Sidebar, SidebarContent } from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarContent>
        <SidebarGroup />
        <SidebarGroup />
      </SidebarContent>
    </Sidebar>
  )
}
```

## SidebarGroup

Use the `SidebarGroup` component to create a section within the sidebar.

A `SidebarGroup` has a `SidebarGroupLabel`, a `SidebarGroupContent` and an optional `SidebarGroupAction`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-group"
    title="Sidebar Group"
    type="block"
    description="A sidebar group."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar group.
  </figcaption>
</figure>

```tsx showLineNumbers
import { Sidebar, SidebarContent, SidebarGroup } from "@/components/ui/sidebar"

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupAction>
            <Plus /> <span className="sr-only">Add Project</span>
          </SidebarGroupAction>
          <SidebarGroupContent></SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  )
}
```

## Collapsible SidebarGroup

To make a `SidebarGroup` collapsible, wrap it in a `Collapsible`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-group-collapsible"
    title="Sidebar Group"
    type="block"
    description="A collapsible sidebar group."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A collapsible sidebar group.
  </figcaption>
</figure>

```tsx showLineNumbers
export function AppSidebar() {
  return (
    <Collapsible defaultOpen className="group/collapsible">
      <SidebarGroup>
        <SidebarGroupLabel asChild>
          <CollapsibleTrigger>
            Help
            <ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" />
          </CollapsibleTrigger>
        </SidebarGroupLabel>
        <CollapsibleContent>
          <SidebarGroupContent />
        </CollapsibleContent>
      </SidebarGroup>
    </Collapsible>
  )
}
```

<Callout>
  **Note:** We wrap the `CollapsibleTrigger` in a `SidebarGroupLabel` to render
  a button.
</Callout>

## SidebarGroupAction

Use the `SidebarGroupAction` component to add an action button to the `SidebarGroup`.

<figure className="flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-group-action"
    title="Sidebar Group"
    type="block"
    description="A sidebar group with an action button."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar group with an action button.
  </figcaption>
</figure>

```tsx showLineNumbers {5-7}
export function AppSidebar() {
  return (
    <SidebarGroup>
      <SidebarGroupLabel asChild>Projects</SidebarGroupLabel>
      <SidebarGroupAction title="Add Project">
        <Plus /> <span className="sr-only">Add Project</span>
      </SidebarGroupAction>
      <SidebarGroupContent />
    </SidebarGroup>
  )
}
```

## SidebarMenu

The `SidebarMenu` component is used for building a menu within a `SidebarGroup`.

A `SidebarMenu` component is composed of `SidebarMenuItem`, `SidebarMenuButton`, `<SidebarMenuAction />` and `<SidebarMenuSub />` components.

<Image
  src="/images/sidebar-menu.png"
  width="716"
  height="420"
  alt="Sidebar Menu"
  className="mt-6 w-full overflow-hidden rounded-lg border dark:hidden"
/>
<Image
  src="/images/sidebar-menu-dark.png"
  width="716"
  height="420"
  alt="Sidebar Menu"
  className="mt-6 hidden w-full overflow-hidden rounded-lg border dark:block"
/>

Here's an example of a `SidebarMenu` component rendering a list of projects.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-menu"
    title="Sidebar Menu"
    type="block"
    description="A sidebar menu with a list of projects."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar menu with a list of projects.
  </figcaption>
</figure>

```tsx showLineNumbers
<Sidebar>
  <SidebarContent>
    <SidebarGroup>
      <SidebarGroupLabel>Projects</SidebarGroupLabel>
      <SidebarGroupContent>
        <SidebarMenu>
          {projects.map((project) => (
            <SidebarMenuItem key={project.name}>
              <SidebarMenuButton asChild>
                <a href={project.url}>
                  <project.icon />
                  <span>{project.name}</span>
                </a>
              </SidebarMenuButton>
            </SidebarMenuItem>
          ))}
        </SidebarMenu>
      </SidebarGroupContent>
    </SidebarGroup>
  </SidebarContent>
</Sidebar>
```

## SidebarMenuButton

The `SidebarMenuButton` component is used to render a menu button within a `SidebarMenuItem`.

### Link or Anchor

By default, the `SidebarMenuButton` renders a button but you can use the `asChild` prop to render a different component such as a `Link` or an `a` tag.

```tsx showLineNumbers
<SidebarMenuButton asChild>
  <a href="#">Home</a>
</SidebarMenuButton>
```

### Icon and Label

You can render an icon and a truncated label inside the button. Remember to wrap the label in a `<span>`.

```tsx showLineNumbers
<SidebarMenuButton asChild>
  <a href="#">
    <Home />
    <span>Home</span>
  </a>
</SidebarMenuButton>
```

### isActive

Use the `isActive` prop to mark a menu item as active.

```tsx showLineNumbers
<SidebarMenuButton asChild isActive>
  <a href="#">Home</a>
</SidebarMenuButton>
```

## SidebarMenuAction

The `SidebarMenuAction` component is used to render a menu action within a `SidebarMenuItem`.

This button works independently of the `SidebarMenuButton` i.e you can have the `<SidebarMenuButton />` as a clickable link and the `<SidebarMenuAction />` as a button.

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton asChild>
    <a href="#">
      <Home />
      <span>Home</span>
    </a>
  </SidebarMenuButton>
  <SidebarMenuAction>
    <Plus /> <span className="sr-only">Add Project</span>
  </SidebarMenuAction>
</SidebarMenuItem>
```

### DropdownMenu

Here's an example of a `SidebarMenuAction` component rendering a `DropdownMenu`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-menu-action"
    title="Sidebar Menu Action"
    type="block"
    description="A sidebar menu action with a dropdown menu."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar menu action with a dropdown menu.
  </figcaption>
</figure>

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton asChild>
    <a href="#">
      <Home />
      <span>Home</span>
    </a>
  </SidebarMenuButton>
  <DropdownMenu>
    <DropdownMenuTrigger asChild>
      <SidebarMenuAction>
        <MoreHorizontal />
      </SidebarMenuAction>
    </DropdownMenuTrigger>
    <DropdownMenuContent side="right" align="start">
      <DropdownMenuItem>
        <span>Edit Project</span>
      </DropdownMenuItem>
      <DropdownMenuItem>
        <span>Delete Project</span>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</SidebarMenuItem>
```

## SidebarMenuSub

The `SidebarMenuSub` component is used to render a submenu within a `SidebarMenu`.

Use `<SidebarMenuSubItem />` and `<SidebarMenuSubButton />` to render a submenu item.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-menu-sub"
    title="Sidebar Menu Sub"
    type="block"
    description="A sidebar menu sub."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar menu with a submenu.
  </figcaption>
</figure>

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuSub>
    <SidebarMenuSubItem>
      <SidebarMenuSubButton />
    </SidebarMenuSubItem>
    <SidebarMenuSubItem>
      <SidebarMenuSubButton />
    </SidebarMenuSubItem>
  </SidebarMenuSub>
</SidebarMenuItem>
```

## Collapsible SidebarMenu

To make a `SidebarMenu` component collapsible, wrap it and the `SidebarMenuSub` components in a `Collapsible`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-menu-collapsible"
    title="Sidebar Menu"
    type="block"
    description="A collapsible sidebar menu."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A collapsible sidebar menu.
  </figcaption>
</figure>

```tsx showLineNumbers
<SidebarMenu>
  <Collapsible defaultOpen className="group/collapsible">
    <SidebarMenuItem>
      <CollapsibleTrigger asChild>
        <SidebarMenuButton />
      </CollapsibleTrigger>
      <CollapsibleContent>
        <SidebarMenuSub>
          <SidebarMenuSubItem />
        </SidebarMenuSub>
      </CollapsibleContent>
    </SidebarMenuItem>
  </Collapsible>
</SidebarMenu>
```

## SidebarMenuBadge

The `SidebarMenuBadge` component is used to render a badge within a `SidebarMenuItem`.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-menu-badge"
    title="Sidebar Menu Badge"
    type="block"
    description="A sidebar menu badge."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar menu with a badge.
  </figcaption>
</figure>

```tsx showLineNumbers
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuBadge>24</SidebarMenuBadge>
</SidebarMenuItem>
```

## SidebarMenuSkeleton

The `SidebarMenuSkeleton` component is used to render a skeleton for a `SidebarMenu`. You can use this to show a loading state when using React Server Components, SWR or react-query.

```tsx showLineNumbers
function NavProjectsSkeleton() {
  return (
    <SidebarMenu>
      {Array.from({ length: 5 }).map((_, index) => (
        <SidebarMenuItem key={index}>
          <SidebarMenuSkeleton />
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  )
}
```

## SidebarSeparator

The `SidebarSeparator` component is used to render a separator within a `Sidebar`.

```tsx showLineNumbers
<Sidebar>
  <SidebarHeader />
  <SidebarSeparator />
  <SidebarContent>
    <SidebarGroup />
    <SidebarSeparator />
    <SidebarGroup />
  </SidebarContent>
</Sidebar>
```

## SidebarTrigger

Use the `SidebarTrigger` component to render a button that toggles the sidebar.

The `SidebarTrigger` component must be used within a `SidebarProvider`.

```tsx showLineNumbers
<SidebarProvider>
  <Sidebar />
  <main>
    <SidebarTrigger />
  </main>
</SidebarProvider>
```

### Custom Trigger

To create a custom trigger, you can use the `useSidebar` hook.

```tsx showLineNumbers
import { useSidebar } from "@/components/ui/sidebar"

export function CustomTrigger() {
  const { toggleSidebar } = useSidebar()

  return <button onClick={toggleSidebar}>Toggle Sidebar</button>
}
```

## SidebarRail

The `SidebarRail` component is used to render a rail within a `Sidebar`. This rail can be used to toggle the sidebar.

```tsx showLineNumbers
<Sidebar>
  <SidebarHeader />
  <SidebarContent>
    <SidebarGroup />
  </SidebarContent>
  <SidebarFooter />
  <SidebarRail />
</Sidebar>
```

## Data Fetching

### React Server Components

Here's an example of a `SidebarMenu` component rendering a list of projects using React Server Components.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-rsc"
    title="Sidebar Menu RSC"
    type="block"
    description="A sidebar menu using React Server Components."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A sidebar menu using React Server Components.
  </figcaption>
</figure>

```tsx showLineNumbers {6} title="Skeleton to show loading state."
function NavProjectsSkeleton() {
  return (
    <SidebarMenu>
      {Array.from({ length: 5 }).map((_, index) => (
        <SidebarMenuItem key={index}>
          <SidebarMenuSkeleton showIcon />
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  )
}
```

```tsx showLineNumbers {2} title="Server component fetching data."
async function NavProjects() {
  const projects = await fetchProjects()

  return (
    <SidebarMenu>
      {projects.map((project) => (
        <SidebarMenuItem key={project.name}>
          <SidebarMenuButton asChild>
            <a href={project.url}>
              <project.icon />
              <span>{project.name}</span>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  )
}
```

```tsx showLineNumbers {8-10} title="Usage with React Suspense."
function AppSidebar() {
  return (
    <Sidebar>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Projects</SidebarGroupLabel>
          <SidebarGroupContent>
            <React.Suspense fallback={<NavProjectsSkeleton />}>
              <NavProjects />
            </React.Suspense>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  )
}
```

### SWR and React Query

You can use the same approach with [SWR](https://swr.vercel.app/) or [react-query](https://tanstack.com/query/latest/docs/framework/react/overview).

```tsx showLineNumbers title="SWR"
function NavProjects() {
  const { data, isLoading } = useSWR("/api/projects", fetcher)

  if (isLoading) {
    return (
      <SidebarMenu>
        {Array.from({ length: 5 }).map((_, index) => (
          <SidebarMenuItem key={index}>
            <SidebarMenuSkeleton showIcon />
          </SidebarMenuItem>
        ))}
      </SidebarMenu>
    )
  }

  if (!data) {
    return ...
  }

  return (
    <SidebarMenu>
      {data.map((project) => (
        <SidebarMenuItem key={project.name}>
          <SidebarMenuButton asChild>
            <a href={project.url}>
              <project.icon />
              <span>{project.name}</span>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  )
}
```

```tsx showLineNumbers title="React Query"
function NavProjects() {
  const { data, isLoading } = useQuery()

  if (isLoading) {
    return (
      <SidebarMenu>
        {Array.from({ length: 5 }).map((_, index) => (
          <SidebarMenuItem key={index}>
            <SidebarMenuSkeleton showIcon />
          </SidebarMenuItem>
        ))}
      </SidebarMenu>
    )
  }

  if (!data) {
    return ...
  }

  return (
    <SidebarMenu>
      {data.map((project) => (
        <SidebarMenuItem key={project.name}>
          <SidebarMenuButton asChild>
            <a href={project.url}>
              <project.icon />
              <span>{project.name}</span>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      ))}
    </SidebarMenu>
  )
}
```

## Controlled Sidebar

Use the `open` and `onOpenChange` props to control the sidebar.

<figure className="mt-6 flex flex-col gap-4">
  <ComponentPreview
    name="sidebar-controlled"
    title="Sidebar Controlled"
    type="block"
    description="A controlled sidebar."
    className="w-full"
  />
  <figcaption className="text-center text-sm text-gray-500">
    A controlled sidebar.
  </figcaption>
</figure>

```tsx showLineNumbers
export function AppSidebar() {
  const [open, setOpen] = React.useState(false)

  return (
    <SidebarProvider open={open} onOpenChange={setOpen}>
      <Sidebar />
    </SidebarProvider>
  )
}
```

## Theming

We use the following CSS variables to theme the sidebar.

```css
@layer base {
  :root {
    --sidebar-background: 0 0% 98%;
    --sidebar-foreground: 240 5.3% 26.1%;
    --sidebar-primary: 240 5.9% 10%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 4.8% 95.9%;
    --sidebar-accent-foreground: 240 5.9% 10%;
    --sidebar-border: 220 13% 91%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }

  .dark {
    --sidebar-background: 240 5.9% 10%;
    --sidebar-foreground: 240 4.8% 95.9%;
    --sidebar-primary: 0 0% 98%;
    --sidebar-primary-foreground: 240 5.9% 10%;
    --sidebar-accent: 240 3.7% 15.9%;
    --sidebar-accent-foreground: 240 4.8% 95.9%;
    --sidebar-border: 240 3.7% 15.9%;
    --sidebar-ring: 217.2 91.2% 59.8%;
  }
}
```

**We intentionally use different variables for the sidebar and the rest of the application** to make it easy to have a sidebar that is styled differently from the rest of the application. Think a sidebar with a darker shade from the main application.

## Styling

Here are some tips for styling the sidebar based on different states.

- **Styling an element based on the sidebar collapsible state.** The following will hide the `SidebarGroup` when the sidebar is in `icon` mode.

```tsx
<Sidebar collapsible="icon">
  <SidebarContent>
    <SidebarGroup className="group-data-[collapsible=icon]:hidden" />
  </SidebarContent>
</Sidebar>
```

- **Styling a menu action based on the menu button active state.** The following will force the menu action to be visible when the menu button is active.

```tsx
<SidebarMenuItem>
  <SidebarMenuButton />
  <SidebarMenuAction className="peer-data-[active=true]/menu-button:opacity-100" />
</SidebarMenuItem>
```

You can find more tips on using states for styling in this [Twitter thread](https://x.com/shadcn/status/1842329158879420864).

## Changelog

### 2024-10-30 Cookie handling in setOpen

- [#5593](https://github.com/shadcn-ui/ui/pull/5593) - Improved setOpen callback logic in `<SidebarProvider>`.

Update the `setOpen` callback in `<SidebarProvider>` as follows:

```tsx showLineNumbers
const setOpen = React.useCallback(
  (value: boolean | ((value: boolean) => boolean)) => {
    const openState = typeof value === "function" ? value(open) : value
    if (setOpenProp) {
      setOpenProp(openState)
    } else {
      _setOpen(openState)
    }

    // This sets the cookie to keep the sidebar state.
    document.cookie = `${SIDEBAR_COOKIE_NAME}=${openState}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`
  },
  [setOpenProp, open]
)
```

### 2024-10-21 Fixed `text-sidebar-foreground`

- [#5491](https://github.com/shadcn-ui/ui/pull/5491) - Moved `text-sidebar-foreground` from `<SidebarProvider>` to `<Sidebar>` component.

### 2024-10-20 Typo in `useSidebar` hook.

Fixed typo in `useSidebar` hook.

```diff showLineNumbers title="sidebar.tsx"
-  throw new Error("useSidebar must be used within a Sidebar.")
+  throw new Error("useSidebar must be used within a SidebarProvider.")
```
````

## File: apps/v4/content/docs/components/skeleton.mdx
````
---
title: Skeleton
description: Use to show a placeholder while content is loading.
component: true
---

<ComponentPreview name="skeleton-demo" description="A skeleton component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add skeleton
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="skeleton" title="components/ui/skeleton.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Skeleton } from "@/components/ui/skeleton"
```

```tsx
<Skeleton className="h-[20px] w-[100px] rounded-full" />
```

## Examples

### Card

<ComponentPreview
  name="skeleton-card"
  description="A card with skeleton showing a loading state."
/>
````

## File: apps/v4/content/docs/components/slider.mdx
````
---
title: Slider
description: An input where the user selects a value from within a given range.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/slider
  api: https://www.radix-ui.com/docs/primitives/components/slider#api-reference
---

<ComponentPreview name="slider-demo" description="A slider component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add slider
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-slider
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="slider" title="components/ui/slider.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Slider } from "@/components/ui/slider"
```

```tsx
<Slider defaultValue={[33]} max={100} step={1} />
```
````

## File: apps/v4/content/docs/components/sonner.mdx
````
---
title: Sonner
description: An opinionated toast component for React.
component: true
links:
  doc: https://sonner.emilkowal.ski
---

<ComponentPreview name="sonner-demo" />

## About

Sonner is built and maintained by [emilkowalski\_](https://twitter.com/emilkowalski_).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps>

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add sonner
```

<Step>Add the Toaster component</Step>

```tsx title="app/layout.tsx" {1,9}
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install sonner next-themes
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="sonner" title="components/ui/sonner.tsx" />

<Step>Add the Toaster component</Step>

```tsx title="app/layout.tsx" {1,9}
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { toast } from "sonner"
```

```tsx
toast("Event has been created.")
```
````

## File: apps/v4/content/docs/components/switch.mdx
````
---
title: Switch
description: A control that allows the user to toggle between checked and not checked.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/switch
  api: https://www.radix-ui.com/docs/primitives/components/switch#api-reference
---

<ComponentPreview name="switch-demo" description="A switch component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add switch
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-switch
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="switch" title="components/ui/switch.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Switch } from "@/components/ui/switch"
```

```tsx
<Switch />
```

## Examples

### Form

<ComponentPreview name="switch-form" />
````

## File: apps/v4/content/docs/components/table.mdx
````
---
title: Table
description: A responsive table component.
component: true
---

<ComponentPreview name="table-demo" description="A table component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add table
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="table" title="components/ui/table.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

```tsx showLineNumbers
<Table>
  <TableCaption>A list of your recent invoices.</TableCaption>
  <TableHeader>
    <TableRow>
      <TableHead className="w-[100px]">Invoice</TableHead>
      <TableHead>Status</TableHead>
      <TableHead>Method</TableHead>
      <TableHead className="text-right">Amount</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell className="font-medium">INV001</TableCell>
      <TableCell>Paid</TableCell>
      <TableCell>Credit Card</TableCell>
      <TableCell className="text-right">$250.00</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## Data Table

You can use the `<Table />` component to build more complex data tables. Combine it with [@tanstack/react-table](https://tanstack.com/table/v8) to create tables with sorting, filtering and pagination.

See the [Data Table](/docs/components/data-table) documentation for more information.

You can also see an example of a data table in the [Tasks](/examples/tasks) demo.
````

## File: apps/v4/content/docs/components/tabs.mdx
````
---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/tabs
  api: https://www.radix-ui.com/docs/primitives/components/tabs#api-reference
---

<ComponentPreview
  name="tabs-demo"
  description="A tabs component with two forms."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add tabs
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-tabs
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="tabs" title="components/ui/tabs.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

```tsx showLineNumbers
<Tabs defaultValue="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">Make changes to your account here.</TabsContent>
  <TabsContent value="password">Change your password here.</TabsContent>
</Tabs>
```
````

## File: apps/v4/content/docs/components/textarea.mdx
````
---
title: Textarea
description: Displays a form textarea or a component that looks like a textarea.
component: true
---

<ComponentPreview name="textarea-demo" description="A textarea" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add textarea
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="textarea" title="components/ui/textarea.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Textarea } from "@/components/ui/textarea"
```

```tsx
<Textarea />
```

## Examples

### Default

<ComponentPreview name="textarea-demo" description="A textarea" />

### Disabled

<ComponentPreview name="textarea-disabled" description="A disabled textarea" />

### With Label

<ComponentPreview
  name="textarea-with-label"
  className="[&_div.grid]:w-full"
  description="A textarea with a label"
/>

### With Text

<ComponentPreview
  name="textarea-with-text"
  description="A textarea with text"
/>

### With Button

<ComponentPreview
  name="textarea-with-button"
  description="A textarea with a button"
/>

### Form

<ComponentPreview name="textarea-form" />
````

## File: apps/v4/content/docs/components/toast.mdx
````
---
title: Toast
description: A succinct message that is displayed temporarily.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/toast
  api: https://www.radix-ui.com/docs/primitives/components/toast#api-reference
---

<Callout title="The toast component has been deprecated." className="mt-0">
  See the [sonner](/docs/components/sonner) documentation for more information.
</Callout>

If you're looking for the old toast component, see the [old docs](https://v3.shadcn.com/docs/components/toast) for more information.
````

## File: apps/v4/content/docs/components/toggle-group.mdx
````
---
title: Toggle Group
description: A set of two-state buttons that can be toggled on or off.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/toggle-group
  api: https://www.radix-ui.com/docs/primitives/components/toggle-group#api-reference
---

<ComponentPreview
  name="toggle-group-demo"
  description="A toggle group with three items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle-group
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-toggle-group
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="toggle-group" title="components/ui/toggle-group.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

```tsx
<ToggleGroup type="single">
  <ToggleGroupItem value="a">A</ToggleGroupItem>
  <ToggleGroupItem value="b">B</ToggleGroupItem>
  <ToggleGroupItem value="c">C</ToggleGroupItem>
</ToggleGroup>
```

## Examples

### Default

<ComponentPreview
  name="toggle-group-demo"
  description="A toggle group with three items."
/>

### Outline

<ComponentPreview
  name="toggle-group-outline"
  description="A toggle group using the outline variant."
/>

### Single

<ComponentPreview
  name="toggle-group-single"
  description="A toggle group with single selection."
/>

### Small

<ComponentPreview
  name="toggle-group-sm"
  description="A toggle group using the small size."
/>

### Large

<ComponentPreview
  name="toggle-group-lg"
  description="A toggle group using the large size."
/>

### Disabled

<ComponentPreview
  name="toggle-group-disabled"
  description="A disabled toggle group."
/>
````

## File: apps/v4/content/docs/components/toggle.mdx
````
---
title: Toggle
description: A two-state button that can be either on or off.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/toggle
  api: https://www.radix-ui.com/docs/primitives/components/toggle#api-reference
---

<ComponentPreview name="toggle-demo" description="A toggle component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-toggle
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="toggle" title="components/ui/toggle.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Toggle } from "@/components/ui/toggle"
```

```tsx
<Toggle>Toggle</Toggle>
```

## Examples

### Default

<ComponentPreview name="toggle-demo" description="A toggle component." />

### Outline

<ComponentPreview
  name="toggle-outline"
  description="A toggle component using the outline variant."
/>

### With Text

<ComponentPreview
  name="toggle-with-text"
  description="A toggle component with text."
/>

### Small

<ComponentPreview name="toggle-sm" description="A small toggle component." />

### Large

<ComponentPreview name="toggle-lg" description="A large toggle component." />

### Disabled

<ComponentPreview
  name="toggle-disabled"
  description="A disabled toggle component."
/>
````

## File: apps/v4/content/docs/components/tooltip.mdx
````
---
title: Tooltip
description: A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/tooltip
  api: https://www.radix-ui.com/docs/primitives/components/tooltip#api-reference
---

<ComponentPreview name="tooltip-demo" description="A tooltip component." />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">CLI</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add tooltip
```

</TabsContent>

<TabsContent value="manual">

<Steps>

<Step>Install the following dependencies:</Step>

```bash
npm install @radix-ui/react-tooltip
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="tooltip" title="components/ui/tooltip.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
```

```tsx showLineNumbers
<Tooltip>
  <TooltipTrigger>Hover</TooltipTrigger>
  <TooltipContent>
    <p>Add to library</p>
  </TooltipContent>
</Tooltip>
```
````

## File: apps/v4/content/docs/components/typography.mdx
````
---
title: Typography
description: Styles for headings, paragraphs, lists...etc
component: true
---

We do not ship any typography styles by default. This page is an example of how you can use utility classes to style your text.

<ComponentPreview
  name="typography-demo"
  description="A collection of typographic elements."
  className="[&_.preview]:!h-auto"
  hideCode
/>

## h1

<ComponentPreview name="typography-h1" />

## h2

<ComponentPreview name="typography-h2" />

## h3

<ComponentPreview name="typography-h3" />

## h4

<ComponentPreview name="typography-h4" />

## p

<ComponentPreview name="typography-p" />

## blockquote

<ComponentPreview name="typography-blockquote" />

## table

<ComponentPreview name="typography-table" />

## list

<ComponentPreview name="typography-list" />

## Inline code

<ComponentPreview name="typography-inline-code" />

## Lead

<ComponentPreview name="typography-lead" />

## Large

<ComponentPreview name="typography-large" />

## Small

<ComponentPreview name="typography-small" />

## Muted

<ComponentPreview name="typography-muted" />
````
