import { Column, Entity, PrimaryColumn } from 'typeorm';

@Entity()
export class $$TEMPLATE$$Entity {
  @PrimaryColumn('uuid')
  versionId: string;

  @Column('text')
  title: string;
}
