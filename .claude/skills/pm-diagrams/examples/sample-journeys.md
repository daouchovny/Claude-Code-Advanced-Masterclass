# Sample User Journeys

Ready-to-use examples for common product scenarios.

---

## 1. SaaS Onboarding Journey

```bash
python3 pm_diagram_gen.py journey \
  --title "SaaS Product Onboarding" \
  --subtitle "B2B software trial to paid conversion" \
  --stages "Discovery,Trial Signup,First Login,Aha Moment,Conversion" \
  --touchpoints "Google Search,Landing Page,Onboarding Wizard,Core Feature,Pricing Page" \
  --emotions "Curious,Hopeful,Overwhelmed,Excited,Evaluating" \
  --actions "Searches for solution,Starts free trial,Explores dashboard,Creates first project,Reviews pricing" \
  --theme default
```

---

## 2. E-Commerce Purchase Journey

```bash
python3 pm_diagram_gen.py journey \
  --title "E-Commerce Purchase Journey" \
  --subtitle "From browsing to repeat purchase" \
  --stages "Browse,Product Discovery,Consideration,Purchase,Post-Purchase" \
  --touchpoints "Homepage,Category Page,Product Detail,Checkout,Order Confirmation" \
  --emotions "Browsing,Interested,Comparing,Anxious,Satisfied" \
  --actions "Views categories,Filters products,Reads reviews,Enters payment,Tracks order" \
  --theme corporate
```

---

## 3. Mobile App User Journey

```bash
python3 pm_diagram_gen.py journey \
  --title "Mobile App Engagement" \
  --subtitle "App store to daily active user" \
  --stages "App Store,Download,First Open,Core Action,Retention" \
  --touchpoints "App Store Listing,Install Screen,Onboarding,Main Feature,Push Notification" \
  --emotions "Interested,Waiting,Exploring,Engaged,Reminded" \
  --actions "Reads reviews,Taps install,Completes setup,Uses feature,Returns to app" \
  --theme dark
```

---

## 4. Customer Support Journey

```bash
python3 pm_diagram_gen.py journey \
  --title "Customer Support Experience" \
  --subtitle "Issue to resolution" \
  --stages "Issue Occurs,Seeks Help,Gets Support,Resolution,Follow-up" \
  --touchpoints "Product,Help Center,Chat/Email,Support Agent,Survey" \
  --emotions "Frustrated,Searching,Waiting,Relieved,Satisfied" \
  --actions "Encounters problem,Searches FAQ,Contacts support,Receives solution,Gives feedback" \
  --theme light
```

---

## 5. B2B Sales Journey

```bash
python3 pm_diagram_gen.py journey \
  --title "Enterprise Sales Journey" \
  --subtitle "Lead to closed deal" \
  --stages "Awareness,Interest,Evaluation,Decision,Purchase" \
  --touchpoints "LinkedIn Ad,Whitepaper,Demo Call,Proposal,Contract" \
  --emotions "Curious,Engaged,Analytical,Negotiating,Committed" \
  --actions "Clicks ad,Downloads content,Attends demo,Reviews terms,Signs contract" \
  --theme corporate
```

---

## 6. Feature Adoption Journey

```bash
python3 pm_diagram_gen.py journey \
  --title "New Feature Adoption" \
  --subtitle "Feature release to power user" \
  --stages "Announcement,Discovery,Trial,Adoption,Advocacy" \
  --touchpoints "Email/In-app,Feature Page,First Use,Regular Use,Share/Review" \
  --emotions "Intrigued,Learning,Experimenting,Productive,Enthusiastic" \
  --actions "Reads announcement,Clicks to learn,Tries feature,Uses daily,Recommends to others" \
  --theme default
```

---

## Tips for Customization

1. **Adjust stage count**: Most journeys work best with 4-6 stages
2. **Match your metrics**: Align stages with your analytics funnel
3. **Use real data**: Replace placeholder emotions with user research
4. **Add context**: Use subtitles to specify the user segment
5. **Choose appropriate themes**:
   - `default`: General purpose, modern look
   - `dark`: Developer/technical audiences
   - `light`: Documentation, print-friendly
   - `corporate`: Executive presentations
